import time
from kafka_client_decorator.client_producer import ClientProducer
import os

from pymongo.mongo_client import MongoClient
CONN_STR, DB, COLLECTION = os.getenv("CONN_STR"), os.getenv("DATABASE"), os.getenv("COLLECTION")
mongo_client = MongoClient(CONN_STR)
db = mongo_client[DB]
COL = db[COLLECTION]

ORDER_KAFKA_TOPIC = "order_details"
ORDER_LIMIT = 15
ORDERS = [{ "items": ["burger", "pizza", "pepsi"]}, 
          { "items": ["pizza", "pepsi"]}, 
          { "items": ["pepsi"]},
          { "items": ["burger", "pizza", "pepsi"]}, 
          { "items": ["pizza", "pepsi"]}
        ]
        
def init_producer():
        """_summary_

        :return: _description_
        :rtype: _type_
        """
        producer = ClientProducer(bootstrap_servers="kafka1:9093", security_protocol="PLAINTEXT")
        print("Going to generate order after 10 seconds")
        print("Generate unique order after every 10 seconds")
        return producer

def find_mongo(food):
        cost = COL.find_one({"name":food}, {"cost":1})
        print(cost)
        return cost["cost"]
        

def main():
        producer = init_producer()
        for i, data in enumerate(ORDERS):
                total_cost = sum([find_mongo(food) for food in data["items"]])
                data['total_cost'] = total_cost
                data["order_id"] = i
                data["user_id"] = f"user_{i}"
                

                producer.produce_to_broker(data, [ORDER_KAFKA_TOPIC])
                print(f"Done sending {data}")
                time.sleep(10)


main()