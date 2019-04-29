# coding:utf-8
from flask import Blueprint,render_template, request
import requests
import os,sys
import json
dirPath = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir,os.pardir))
sys.path.append(dirPath)
from service.es.search import Search
from flask_cors import CORS
es = Blueprint('es',__name__)
CORS(es, resources=r'/*')

@es.route('/table')
def table():
    name = request.values['name']
    return json.dumps(Search().table(name))

