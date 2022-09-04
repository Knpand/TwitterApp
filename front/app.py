from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import Flask, render_template, jsonify, request, make_response
from flask_restful import Api, Resource
from flask_cors import CORS
from random import *
from sql import SQLhandler

sqlhandler = SQLhandler()
app = Flask(__name__)

# @app.route("/")
# def index():
#     sqldatails=sqlhandler.select_all()
#     print(sqldata)
#     return sqldata

@app.route("/")
def form():
    return render_template("form.html")

@app.route("/form2")
def form2():
    print(sqlhandler.select_all())
    return render_template("form2.html")

@app.route("/form3")
def form3():
    print(sqlhandler.select_all())
    return render_template("form3.html")

@app.route("/insert_data", methods=["POST"])
def insert_data():
    try:
        sentence=request.form["sentence"]
        sqlhandler.insert_sentence(sentence)
        return redirect("/form2")
    except:
        return redirect("/form3")
