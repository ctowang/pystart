from pykafka import KafkaClient
host = '192.168.213.25:27004,192.168.213.25:27005'
client = KafkaClient(hosts = host)  
print(client.topics)
print("_________________________")
topic = client.topics['logstash_yangchen']
producer = topic.get_producer()
for i in range(4):
    message = str('test: %s'%(i))
    producer.produce(bytes(message,encoding='utf-8'))
producer.stop()
