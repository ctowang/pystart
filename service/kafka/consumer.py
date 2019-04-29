from pykafka import KafkaClient
host = '192.168.213.25:27004,192.168.213.25:27005'
client = KafkaClient(hosts = host)  
print(client.topics)
print("_________________________")
topic = client.topics['logstash_yangchen']
#consumer = topic.get_balanced_consumer(consumer_group='testgroup',auto_commit_enable=True')
consumer = topic.get_simple_consumer()
for message in consumer:
    if message is not None:
        valuestr = message.value.decode() 
        print(valuestr)
