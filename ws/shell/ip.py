# coding:utf-8
from flask import Blueprint,render_template, request
import os,sys
dirPath = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir,os.pardir))
sys.path.append(dirPath)
from flask_cors import CORS
ip = Blueprint('ip',__name__)
CORS(ip, resources=r'/*')


@ip.route('/ips')
def ips():
    val = os.popen('sh service/shell/ip.sh').read()
    print(val)
    return val 

