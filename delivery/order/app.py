#!/usr/bin/python

from flask import Flask, jsonify 
import json
import requests

order_list='''
[
    {
        "id":"1",
        "name":"맥도날드 햄버거",
        "store":"한국 맥도날드",
        "storeId": "100",
        "price": 8700,
        "img":"https://joinc-edu.s3.ap-northeast-2.amazonaws.com/docker-msa/ham-01.jpeg"
    },
    {
        "id":"2",
        "name":"좋은날 떡복이",
        "store":"좋은음식",
        "storeId": "101",
        "price": 5000,
        "img":"https://joinc-edu.s3.ap-northeast-2.amazonaws.com/docker-msa/tteokbokki.jpeg"
    },
    {
        "id":"3",
        "name":"우리 돈까스",
        "store":"우리돈",
        "storeId": "102",
        "price": 11000,
        "img":"https://joinc-edu.s3.ap-northeast-2.amazonaws.com/docker-msa/pork_cutlet.jpg"
    },
    {
        "id":"4",
        "name":"빅맥 세트",
        "store":"롯데리아",
        "storeId": "103",
        "price": 15000,
        "img":"https://joinc-edu.s3.ap-northeast-2.amazonaws.com/docker-msa/ham-02.jpeg"
    }
]
'''

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
@app.route("/api/order", methods=["GET"])
def products():
    data = json.loads(order_list)
    return jsonify(data)

@app.route("/api/order/<oid>", methods=["GET"])
def order(oid):
    sid="0"
    data = json.loads(order_list)
    for v in data: 
        if v["id"]==oid:
            sid=v["storeId"]
    response = requests.get("http://store:9003/api/store/"+sid)
    store_status = json.loads(response.content)
    return store_status 

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=9001,
        debug=True
    )

