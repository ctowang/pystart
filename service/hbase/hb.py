# coding=utf-8
import happybase
 
#connection = happybase.Connection('153.35.93.31',autoconnect=False,table_prefix='myhbs')
connection = happybase.Connection('153.35.93.31',autoconnect=False)
connection.open()
print (connection.tables())


#connection.create_table(
#    'myhbs',
#    {
#        'cf1': dict(max_versions=10),
#        'cf2': dict(max_versions=1, block_cache_enabled=False),
#        'cf3': dict(),  
#    }
#)
#创建表
#table = connection.table('myhbs')


#创建表
#connection.create_table(
#'wangy',
#{
#"info":{}
#}
#)

table = connection.table('wangy')

#table.put("yc",{"info:pm10":"100"})
#table.put("yc",{"info:pm2.5":"68"})
#table.put("yc",{"info:id":"hz-yc-10021"})




#table.put("wy1",{"info:name":"liuli"})
#table.put("wy1",{"info:name":"gmx"})
#table.put("wy1",{"info:date":"2019"})
#删除整行
#table.delete("wy1")
#删除一个列族
#table.delete("wy1", columns=["info:name"])

#查看行数据
#row = table.row("yc")
#print(row)
#row = table.rows(["wy1","wy2"])


#nm = row[b'info:data'].decode('utf-8')

#print (nm)




#query = table.scan(limit=2)
#result = list(query)

#print (result)

#扫描全表
#for key, value in table.scan():
#    print (key,value)
#扫描row之间
#for key, value in table.scan(row_start='wy1', row_stop='wy3'):
#    print (key, value)





#删除表
#connection.delete_table("liuli", True)


#data = {'cf2:name': u'hupeng', 'cf2:date': '2017-03-11'}

#table.put(row='wonter', data=data)

#for key, value in table.scan():
#    print (key, value)

#for key, value in table.scan(row_start='wonter'):
#    print (type(value))
    
#for key in table.scan():
#    print (key)

connection.close()
