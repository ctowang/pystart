# coding:utf-8
from flask import Blueprint,render_template, request
import requests
from flask_cors import CORS
qx = Blueprint('qxsp',__name__)
CORS(qx, resources=r'/*')

@qx.route('/sp')
def sp():
    url = 'http://218.94.29.146:85/home/login?service=http%3A%2F%2F218.94.29.146%3A85%2Fhome%2Findex.action&username=qxaj&password=73EC3AB1489E617A54182EECCFF91151&pwdLevel=2&loginWay=1&clientIP=10.1.1.1&serviceIP=10.1.1.1&codeId=c49506fc-0ef2-42dc-8d1e-b89d1bc6646e&vCode=2a8aeab8-ef8e-4cf1-bd20-dc92b3a441ce&clientMAC=+&loginType=3&_eventId=submit&errorCode='
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Cookie':'CAS-USERNAME=qxaj; JSESSIONID=817D551E7890417870AD7DAFF027FBC4'
}
    session = requests.Session()
    res = session.post(url=url, headers=headers, allow_redirects=False)
    #return res.headers['location'].split("=")[1]
    print(res.cookies['CASTGC'])
    return res.cookies['CASTGC']

if __name__ == "__main__":
    sp()
