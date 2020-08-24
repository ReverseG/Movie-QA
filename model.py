import jieba
import jieba.posseg as psg
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB


class QuestionPrediction:
    """
    jieba加载自定义词典进行分词
    再通过TfidfVectorizer向量化训练贝叶斯模型
    """
    def __init__(self):
        dict_file, template_file  = './data/dictionary.csv', './data/question.csv'
        jieba.load_userdict(dict_file)
        psg
        train_x, train_y = self.read_data(template_file)
        self.tv, self.model = self.train(train_x, train_y)

    def read_data(self, path):
        data = pd.read_csv(path)
        train_x = list()
        for s in data['question']:
            segs = [x.word for x in psg.lcut(s)]
            train_x.append(' '.join(segs))
        train_y = data['label'].tolist()
        return train_x, train_y

    def train(self, train_x, train_y):
        tv = TfidfVectorizer()
        feature_x = tv.fit_transform(train_x).toarray()
        label_y = train_y
        model = MultinomialNB(alpha=0.01)
        model.fit(feature_x, label_y)
        return tv, model

    def predict(self, question):
        filling_segs = []
        feature_x = []
        for seg in psg.lcut(question):
            if seg.flag in ['nr', 'nm', 'ng']:
                feature_x.append(seg.flag)
                filling_segs.append(seg)
            else:
                feature_x.append(seg.word)
        feature_x = ' '.join(feature_x)
        print(feature_x)
        feature_x = self.tv.transform([feature_x]).toarray()
        label = self.model.predict(feature_x)
        return label[0], filling_segs


if __name__ == '__main__':
    model = QuestionPrediction()
    label = model.predict('周润发参演的电影有哪些？')
    print(label)


