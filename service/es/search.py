#coding=utf-8
import json
import os,sys
dirPath = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir,os.pardir))
sys.path.append(dirPath)
from service.es.es import Es
class Search():
  def tables(self):
    #查看所有索引
    print(Es().es().cat.indices())

  def table(self,name):
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
    response = Es().es().search(index=name,body=body)
    print (response)
    return response

if __name__ == '__main__':
    Search().table("my-index")
