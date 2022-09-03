from flask import Flask

from flask import Flask, render_template, jsonify, request, make_response
from flask_restful import Api, Resource
from flask_cors import CORS
from random import *
from sql import SQLhandler

sqlhandler = SQLhandler()
app = Flask(__name__)

@app.route("/")
def index():
    sqldatails=sqlhandler.select_all()
    print(sqldata)
    return sqldata