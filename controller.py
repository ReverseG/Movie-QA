from flask import Flask, render_template, request
import json

app = Flask(__name__, template_folder='template')


@app.route("/question")
def question():
    return render_template('search.html')


@app.route("/search")
def search():
    key = request.args.get('wd')
    print(key)
    res = {
        'data': key
    }
    return json.dumps(res)


if __name__ == '__main__':
    app.run()
