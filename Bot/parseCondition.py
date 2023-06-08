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
import pandas as pd
import pandas_ta as ta
from pymongo import MongoClient
from tvDatafeed import TvDatafeed, Interval
tv = TvDatafeed()



dotenv.load_dotenv()
mongo_url = os.getenv("MONGO_URL")

client = MongoClient(mongo_url)
db = client["blockchain"]
col = db["data"]



  
def get_btc_data():
  data =  tv.get_hist(symbol='BTCUSDT.P',exchange='Binance',interval=Interval.in_15_minute,n_bars=1000)
  data = data.rename(columns={"datetime":"Date","open":"PriceOpen","high":"PriceHigh","low":"PriceLow","close":"PriceClose","volume":"Volume"})
  
  # adding few indicators to the data
  #macd 12,26 
  macD = ta.macd(data["PriceClose"], length_fast=12, length_slow=26, append=True)
  data["MACD 12,26"] = macD["MACD_12_26_9"]

  return data


def add_ema(length, data):
  # checking if we have already added the ema column
  if "EMA_"+str(length) in data.columns:
    return data
  
  ema = ta.ema(data["PriceClose"], length=length, append=True)
  data["EMA_"+str(length)] = ema
  return data
  
  
def add_rsi(length, data):
  # checking if we have already added the rsi column
  if "RSI_"+str(length) in data.columns:
    return data
  
  rsi = ta.rsi(data["PriceClose"], length=length, append=True)
  data["RSI_"+str(length)] = rsi
  return data


def add_sma(length, data):
  # checking if we have already added the sma column
  if "SMA_"+str(length) in data.columns:
    return data
  
  sma = ta.sma(data["PriceClose"], length=length, append=True)
  data["SMA_"+str(length)] = sma
  return data



  
def parsing_the_data(jsonData):
  # Taking Main Values
  # binance_api = jsonData["binance_api"]
  # binance_secret = jsonData["binance_secret"]
  # discord_webhook = jsonData["discord_webhook"]
  # takeProfit = jsonData["takeProfit"]
  # stopLoss = jsonData["stopLoss"]


  neutral_indicators = ["PriceOpen", "PriceHigh", "PriceLow", "PriceClose", "MACD 12,26"]

  advanced_indicators = ["EMA", "RSI", "SMA"]


  # Taking Conditions
  conditions = jsonData["conditions"]
  for i in conditions:
    indicator = i.get("indicator")
    length = i.get("length")
    condition = i.get("condition")
    choice = i.get("choice")
    indicator2 = i.get("indicator2")
    length2 = i.get("length2")
    constantValue = i.get("constantValue")
    
    condition1 = ""
    condition2 = ""
    
    if indicator in advanced_indicators:
      length = int(length)
      if indicator == "EMA":
        data = add_ema(length, data)
      elif indicator == "RSI":
        data = add_rsi(length, data)
      elif indicator == "SMA":
        data = add_sma(length, data)
        
        
    if indicator2 in advanced_indicators:
      length2 = int(length2)
      if indicator2 == "EMA":
        data = add_ema(length2, data)
      elif indicator2 == "RSI":
        data = add_rsi(length2, data)
      elif indicator2 == "SMA":
        data = add_sma(length2, data)
      
     
  
  
print(parsing_the_data(condition))