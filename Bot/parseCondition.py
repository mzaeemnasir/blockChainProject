condition = {
  "conditions": [
    {
      "indicator": "PriceOpen",
      "length": "",
      "condition": "Greater Than Or Equal",
      "choice": "Indicator",
      "indicator2": "PriceHigh",
      "length2": "",
      "constantValue": ""
    },  
    {
      "indicator": "PriceOpen",
      "length": "",
      "condition": "Greater Than Or Equal",
      "choice": "Indicator",
      "indicator2": "PriceHigh",
      "length2": "",
      "constantValue": ""
    }
  ],
  "takeProfit": "123",
  "stopLoss": "1231",
  "binance_api": "123123",
  "binance_secret": "print(e)",
  "discord_webhook": "1231231",
}


import json
from pymongo import MongoClient

url = "mongodb+srv://hitman:zaeem123@cluster0.rmbcl.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(url)

db = client["blockchain"]
col = db["data"]


def get_data():
  data = col.find_one()
  return data
  
def add_data():
  data = col.insert_one(condition)
  return data
  
  
def parsing_the_data(jsonData):
  indicator1 = jsonData["conditions"][0]["indicator"]
  
  
  
  
print(add_data())