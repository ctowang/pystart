#coding=utf-8
from elasticsearch import Elasticsearch
class Es():
  def es(self):
    #es连接
    es = Elasticsearch(
        ['192.168.213.23:27022', '192.168.213.23:27023'],
        sniff_on_start=True,
        sniff_on_connection_fail=True,
        sniffer_timeout=60
    )
    return es
