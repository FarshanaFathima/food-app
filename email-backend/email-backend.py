import json
from kafka import KafkaConsumer

ORDER_CONFIRMED_TOPIC = "order_confirmed"

consumer = KafkaConsumer(ORDER_CONFIRMED_TOPIC, bootstrap_servers="kafka:9092")
print(f"Going to start listening from {ORDER_CONFIRMED_TOPIC}")
while True:
    for messages in consumer:
        consumed_message = json.loads(messages.value.decode())
        print(f"Confirmed transaction {consumed_message}")