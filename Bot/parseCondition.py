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
  "binance_api":"e884248f986f1d587d8cfa36ff86271d04bafb10760399afd683bcad9936eb31",
  "binance_secret":"051b2190c5781275fd8948c99f832de2c6069a2018fa3d7b57d30cd0c34ad972",
  "discord_webhook":"123123123",
}

condition2 = {
              "conditions":[{"indicator":"PriceOpen","length":"",
              "condition":"Equal","value":"",
              "choice":"ConstantValue",
              "constantValue":"26600"}],
              "takeProfit":"1.5","stopLoss":"1"}


import json, dotenv, os
from pymongo import MongoClient

dotenv.load_dotenv()
mongo_url = os.getenv("MONGO_URL")

client = MongoClient(mongo_url)
db = client["blockchain"]
col = db["data"]

  
  
def parsing_the_data(jsonData):
  # Taking Main Values
  binance_api = jsonData["binance_api"]
  binance_secret = jsonData["binance_secret"]
  discord_webhook = jsonData["discord_webhook"]
  takeProfit = jsonData["takeProfit"]
  stopLoss = jsonData["stopLoss"]


  # Taking Conditions
  conditions = jsonData["conditions"]
  for i in conditions:
    indicator = i.get("indicator") 
    length = i.get("length")
    condition = i.get("condition")
    choice = i.get("choice")
    constantValue = i.get("constantValue")
    indicator2 = i.get("indicator2")
    length2 = i.get("length2")
    value = i.get("value")

    if choice.lower() == "constantvalue":
      value = constantValue
      
      
    if choice.lower() == "indicator":
      value = indicator2

  
  
print(parsing_the_data(condition2))