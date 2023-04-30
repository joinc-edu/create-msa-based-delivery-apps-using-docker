#!/usr/bin/python

from flask import Flask, jsonify, session, request, redirect
import json

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route("/api/user", methods=["POST"])
def login():
    session['username'] = request.form['username']
    return redirect("/w/login", code=302)

@app.route("/api/user", methods=["GET"])
def get():
    if "username" in session:
        print(session["username"])
        return ("session found:"+session["username"])
    else:
        return ("Session not found: ")

@app.route("/api/user/logout", methods=["GET"])
def logout():
    session.clear()
    return redirect("/w/login", code=302)

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=9002,
        debug=True
    )

