#!/usr/bin/python

from flask import Flask

app = Flask(__name__)

@app.route("/user/<name>", methods=["GET"])
def index(name):
    return "Hello world! %s" % name


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8088,
        debug=True
    )
