# coding:utf-8
import pymysql
import os,sys
dirPath = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir,os.pardir))
sys.path.append(dirPath)
from configparser import ConfigParser

cp = ConfigParser()
cp.read("../../config/db.cfg")
section = cp.items('mysql')

sid = cp.get('mysql', 'db')
ip = cp.get('mysql', 'host')
name = cp.get('mysql', 'user')
pwd = cp.get('mysql', 'passwd')
pt = cp.getint('mysql', 'port')



db = pymysql.connect(host=ip,port=pt,user=name,passwd=pwd,db=sid)
cursor = db.cursor()
sql = "SELECT * FROM project"
try:
   cursor.execute(sql)
   results = cursor.fetchall()
   for row in results:
      print(row[2])
except:
   print ("Error: unable to fetch data")
db.close()
