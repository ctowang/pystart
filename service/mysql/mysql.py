import pymysql
db = pymysql.connect(host='192.168.213.16',port = 28007,user='root',passwd='hz789123',db = 'api')
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
