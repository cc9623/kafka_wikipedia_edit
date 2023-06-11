from kafka import KafkaConsumer
import json
from datetime import datetime

# Initialisiere den Kafka Consumer
consumer = KafkaConsumer(
    'wikipedia-edits',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda v: json.loads(v.decode('utf-8')),
    auto_offset_reset='earliest',
    group_id='wiki-consumer-group')

# Führe Zähler dicts ein für die Aggregationen, einmal deutsch, einmal alle sprachen
global_edit_counts = {}
german_edit_counts = {}

# Funktion, um timestampe in Minuten umzuwandeln
def timestamp_to_minute(ts):
    return datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M')

# Lese die Nachrichten aus dem Kafka-Stream
for message in consumer:
    value = message.value
    minute = timestamp_to_minute(value['timestamp'])

    # Zähle die globalen Edits pro Minute
    if minute not in global_edit_counts:
        global_edit_counts[minute] = 0
    global_edit_counts[minute] += 1

    # Zähle die Edits der deutschen Wikipedia pro Minute
    if value['language_german'] == 1:
        if minute not in german_edit_counts:
            german_edit_counts[minute] = 0
        german_edit_counts[minute] += 1

    # Ausgabe der Aggregationen
    print(f"Global edit counts: {global_edit_counts}")
    print(f"German edit counts: {german_edit_counts}")
