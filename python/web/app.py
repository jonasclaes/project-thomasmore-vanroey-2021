from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello world! Test</p>"
