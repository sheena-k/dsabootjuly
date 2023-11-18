from flask import Flask, render_templates

app = Flask(__name__)

@app.route('/')
def hello():
    return render_templates('index.html')

@app.route('/name')
def hey():
    return ('How are you')


if __name__ == '__main__':
    app.run()