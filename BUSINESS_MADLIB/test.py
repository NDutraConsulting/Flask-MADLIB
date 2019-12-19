import os
from flask import Flask, render_template, g, request, redirect
app = Flask(__name__)

@app.route("/madlib1")
def hello():
    return render_template('madlib.html')

if __name__ == "__main__":
    app.run()
