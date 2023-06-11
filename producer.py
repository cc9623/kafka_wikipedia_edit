from kafka import KafkaProducer
import json
import time
import random

#import data_prep to use simplified data
import data_prep

# Initialisiere den Kafka Producer
producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))


data = dict(data_prep.df)
# iteriere über data und sende sie an das Kafka-Topic, muss type int sein
for i in range(len(data['id'])):
    message = {
        'id': int(data['id'][i]),
        'timestamp': int(data['timestamp'][i]),
        'language_german': int(data['language_german'][i])
    }
    producer.send('wikipedia-edits', value=message)
    producer.flush() # sichert, dass alle asynchronen Nachrichten gesendet wurden
    time.sleep(random.random()) # Warte zufällige Zeit zwischen 0-1 Sekunde