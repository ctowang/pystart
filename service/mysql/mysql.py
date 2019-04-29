# coding:utf-8
import pymysql
import os,sys
dirPath = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir,os.pardir))
sys.path.append(dirPath)
from configparser import ConfigParser

#≥ı ºªØconfig¿‡
cp = ConfigParser()
cp.read("../../config/db.cfg")
section = cp.sections()[0]

sid = cp.get(section, "db")
ip = cp.get(section, "host")
name = cp.get(section, "user")
pwd = cp.get(section, "passwd")
pt = cp.getint(section, "port")



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
