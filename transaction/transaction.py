ORDER_KAFKA_TOPIC = "order_details"
ORDER_CONFIRMED_TOPIC = "order_confirmed"
SALES = 0
from kafka_client_decorator.kafka_client import KafkaClient, ClientProducer
consumer_client = KafkaClient(bootstrap_servers="kafka1:9093",
                              security_protocol="PLAINTEXT",max_poll_interval_ms=1800000)


producer = ClientProducer(bootstrap_servers="kafka1:9093", security_protocol="PLAINTEXT")
print("Going to start listening")

@consumer_client.consumer_producer(consumer_from_topic=ORDER_KAFKA_TOPIC, group_id="bank_statement")
def process(consumed_message=None):
    global SALES
    user_id = consumed_message["user_id"]
    total_cost = consumed_message["total_cost"]
    SALES += total_cost
    data = {
        "customer_id":user_id,
        "customer_email":f"{user_id}@gmail.com",
        "total_cost":total_cost
    }
    print('Successful transaction consumed')
    producer.produce_to_broker(data, [ORDER_CONFIRMED_TOPIC])
    print(f'Sales now ${SALES}')
    # producer.send(ORDER_CONFIRMED_TOPIC, json.dumps(data).encode("utf-8"))
    # time.sleep(10)

process()