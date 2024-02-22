import time

from kafka_client_decorator.client_producer import ClientProducer

ORDER_KAFKA_TOPIC = "order_details"
ORDER_LIMIT = 15

#instantiate producer, this will write to kafka

producer = ClientProducer(bootstrap_servers="kafka1:9093", security_protocol="PLAINTEXT")
print("Going to generate order after 10 seconds")
print("Generate unique order after every 10 seconda")


for i in range(1, ORDER_LIMIT):
    data = {"order_id":1, 
            "user_id": f"tom_{i}",
            "total_cost": i*2,
            "items": "burger, pizza"
            }

    producer.produce_to_broker(data, [ORDER_KAFKA_TOPIC])
    print(f"Done sending {data}")
    time.sleep(10)