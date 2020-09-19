from flask import Flask, render_template, request, g
import json
from search import SearchRobot


app = Flask(__name__, template_folder='template')


def get_robot():
    if 'robot' not in g:
        g.robot = SearchRobot()
    return g.robot


@app.route("/question")
def question():
    return render_template('search.html')


@app.route("/knowledge")
def knowledge():
    return render_template('knowledge.html')


@app.route("/robot_page")
def robot_page():
    return render_template('robot_page.html')


@app.route("/robot")
def robot():
    return render_template('robot.html')


@app.route("/index")
def index():
    return render_template('index.html')


@app.route("/search")
def search():
    robot = get_robot()
    question = request.args.get('spoken')
    answer = robot.ask(question)
    res = {
        'data': answer
    }
    return json.dumps(res)


if __name__ == '__main__':
    app.run()
