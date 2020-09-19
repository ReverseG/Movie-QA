from py2neo import Graph
import pandas as pd
from model import QuestionPrediction


class SearchRobot:
    def __init__(self):
        self.graph = Graph(host='10.170.129.77', auth=('neo4j', '123456'))
        self.cypher_template = self.get_cypher_template('./data/cypher_template.csv')
        self.model = QuestionPrediction()

    def get_cypher_template(self, path):
        csv =pd.read_csv(path)
        key = csv['qt']
        value = csv['cypher']
        return dict(zip(key, value))

    def search(self, question_type, filling_segs):
        template = self.cypher_template.get(question_type)
        template = str(template)
        for seg in filling_segs:
            template = template.replace(seg.flag, seg.word, 1)
        data = self.graph.run(template).data()
        res = ','.join([x['name'] for x in data])
        return res

    def ask(self, question):
        type, segs = self.model.predict(question)
        answer = self.search(type, segs)
        return answer


# if __name__ == '__main__':
#     model = QuestionPrediction()
#     robot = SearchRobot()
#     for _ in range(10):
#         question = input()
#         question_type, filling_segs = model.predict(question)
#         print(question_type)
#         print(filling_segs)
#         res = robot.search(question_type, filling_segs)
#         print(res)

