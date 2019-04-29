# coding:utf-8
from flask import Blueprint,render_template, request
import requests
import os,sys
dirPath = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir,os.pardir))
sys.path.append(dirPath)
from service.wy import wy
from flask_cors import CORS
test = Blueprint('test',__name__)
CORS(test, resources=r'/*')

@test.route('/htm')
def htm():
    user = { 'nickname': 'Miguel' }
    return '''
<html>
  <head>
    <title>Home Page</title>
  </head>
  <body>
    <h1>Hello, ''' + user['nickname'] + '''</h1>
  </body>
</html>
'''
@test.route('/cs')
def cs():
    user = request.values['user']
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


if __name__ == "__main__":
    dy()
