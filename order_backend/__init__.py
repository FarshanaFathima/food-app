from pymongo.mongo_client import MongoClient
mongo_client = MongoClient("mongodb", 27017)
db = mongo_client["food-db"]
COL = db["menu-rate"]
