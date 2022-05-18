from flask import Flask

app = Flask(__name__)

myvariable = 'Hello world!'

@app.route('/')
def hello_world():
    return myvariable

