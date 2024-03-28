from flask import Flask, jsonify, request, render_template

from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)


@app.route("/home", methods = ['GET'])
def home():
    return jsonify({'text':"Hi"})


@app.route("/home/<data>", methods = ['GET'])
def home2(data):
    return jsonify({'text':data})