#coding=utf-8
import json
from es import Es

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
Es().es().index(index="logstash_ftp",doc_type="doc",body=mymapping)
Es().es().index(index="logstash_ftp",doc_type="doc",body=mymapping2)

