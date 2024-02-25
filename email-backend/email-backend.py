from kafka_client_decorator.kafka_client import KafkaClient, ClientProducer

ORDER_CONFIRMED_TOPIC = "order_confirmed"

consumer = KafkaClient(bootstrap_servers="kafka1:9093",
                              security_protocol="PLAINTEXT",max_poll_interval_ms=1800000)
print(f"Going to start listening from {ORDER_CONFIRMED_TOPIC}")

@consumer.consumer_producer(consumer_from_topic=ORDER_CONFIRMED_TOPIC, group_id="bank_statement")
def process(message=None):
    email = message["customer_email"]
    cost = message["total_cost"]
    print(f"{email} your order is confirmed, please pay {cost}")
 
process()