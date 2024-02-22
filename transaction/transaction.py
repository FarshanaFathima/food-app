import json
import kafka
import time

from kafka import KafkaConsumer
from kafka import KafkaProducer

ORDER_KAFKA_TOPIC = "order_details"
ORDER_CONFIRMED_TOPIC = "order_confirmed"

from kafka_client_decorator.kafka_client import KafkaClient, ClientProducer
consumer_client = KafkaClient(bootstrap_servers="kafka1:9093",
                              security_protocol="PLAINTEXT",max_poll_interval_ms=1800000)


# producer = KafkaProducer(bootstrap_servers="kafka:9092")
print("Going to start listening")

@consumer_client.consumer_producer(
    consumer_from_topic=ORDER_KAFKA_TOPIC, group_id="bank_statement"
)
producer = ClientProducer(bootstrap_servers="kafka1:9093", security_protocol="PLAINTEXT")
def process(consumed_message=None):
    # for message in consumer:
    #     print("Ongoing transaction..")
    #     consumed_message = json.loads(message.value.decode())
    #     print(consumed_message)
    user_id = consumed_message["user_id"]
    total_cost = consumed_message["total_cost"]
    
    data = {
        "customer_id":user_id,
        "customer_email":f"{user_id}@gmail.com",
        "total_cost":total_cost
    }
    print('Successful transaction consumed')
    producer.produce_to_broker(data, [ORDER_CONFIRMED_TOPIC])
    # producer.send(ORDER_CONFIRMED_TOPIC, json.dumps(data).encode("utf-8"))
    # time.sleep(10)

process()