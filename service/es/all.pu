#coding=utf-8
from elasticsearch import Elasticsearch
import json
#es连接
es = Elasticsearch(
    ['192.168.213.23:27022', '192.168.213.23:27023'],
    sniff_on_start=True,
    sniff_on_connection_fail=True,
    sniffer_timeout=60
)

#查看所有索引
#print(es.cat.indices())

#mymapping = {
#                    'type': 'text',
#                    'analyzer': 'ik_max_word'
#}

mymapping = {

"licensePlate": "苏AJ9608",
"projectName": "qx15jxm",
"path": "/var/log/messages",
"singId": "20190428091711437",
"host": "host-192-168-213-15",
"licenseType": "-1",
"@timestamp": "2019-03-27T09:53:07.444Z",
"@version": "1",
"licensePlateColor": "黄",
"licensePlateImg": "/qx15jxm/1/qx15jxm_20190428091711437_苏AJ9608_黄.jpg",
"dateTime": "2019-04-28T09:17:11.803Z",
"inserttime":"2019-04-28 09:17:07"
}

mymapping2 = {

"licensePlate": "苏AJ9608",
"projectName": "qx15jxm2",
"path": "/var/log/messages",
"singId": "20190425145416426",
"host": "host-192-168-213-15",
"licenseType": "-1",
"@timestamp": "2019-03-27T09:53:07.444Z",
"@version": "1",
"licensePlateColor": "黄",
"licensePlateImg": "/qx15jxm2/1/qx15jxm2_2019042809171668_苏AJ9608_黄.jpg",
"dateTime": "2019-04-28T09:17:11.803Z",
"inserttime":"2019-04-28 09:17:07"
}

#创建新的索引,追加数据
es.index(index="logstash_ftp",doc_type="doc",body=mymapping)
es.index(index="logstash_ftp",doc_type="doc",body=mymapping2)

body = {
  "query": {
    "bool": {
      "must": [
        {
          "match_all": {}
        }
      ],
      "must_not": [],
      "should": []
    }
  },
  "from": 0,
  "size": 10,
  "sort": [],
  "aggs": {}
}

#查看索引内容
#response = es.search(index="my-index",body=body)
#print (response)

#根据id删除数据
id = "HcF6U2oBtDDB1EOyY741"
#id = response['hits']['hits']
#print (id[0]['_id'])
#es.delete(index='logstash_ftp', doc_type='doc',id=id)

#根据id更新数据
newmymapping = {
                     "doc":{
                    'search_analyzer': 'wangyong'
                      }
}
#es.update(index="my-index",doc_type="doc",id="xvP0SWoBsysL4MofaqNE",body=newmymapping)



