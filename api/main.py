# from typing import Union

# from enum import Enum
from fastapi import FastAPI, status, Body, HTTPException
import motor.motor_asyncio
from pydantic import BaseModel, Field, ConfigDict, field_validator, model_validator
import os

# class Beverages(str, Enum):
#     PEPSI="pepsi"
#     FANTA="fanta"
#     COKE="coke"

# app = FastAPI()


# @app.get("/status")
# async def check_status():
#     return {"Hello": "World"}

# @app.get("/food-app/order-beverages")
# async def get_customer_name(beverage:Beverages):
#     print(beverage)
#     return [{"id":1, "name":"fars"}, {"id":2, "name":"shah"}]
CONN_STR, DB, COLLECTION = os.getenv("CONN_STR"), os.getenv("DATABASE"), os.getenv("COLLECTION")
client = motor.motor_asyncio.AsyncIOMotorClient(CONN_STR)
db = client[DB]
order_collection = db[COLLECTION    ]

class Order(BaseModel):
    Drinks : int = Field(default=0, ge=0)
    Pizza : int = Field(default=0, ge=0)
    Burger: int = Field(default=0, ge=0)
    
    @classmethod
    def validate(cls, order_data):
        total_order = order_data["Drinks"] + order_data["Pizza"] + order_data["Burger"]
        if total_order <= 0:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Total order must be greater than 0")
        
    
app = FastAPI(title="Food Ordering API", summary="A mini project to understand and apply API concepts")

@app.post("/food-order/", response_description="Place a new Order", status_code=status.HTTP_201_CREATED)
async def place_order(order:Order=Body(...)):
    """Place a new order

    :param order: _description_, defaults to Body(...)
    :type order: Order, optional
    """
    print(type(order), order)
    data = order.model_dump()
    order.validate(data)
    new_order = await order_collection.insert_one(data)
    return {"id_": str(new_order.inserted_id)}
    