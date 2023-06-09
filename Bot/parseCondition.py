import json, dotenv, os
import pandas as pd
import pandas_ta as ta
from pymongo import MongoClient
from tvDatafeed import TvDatafeed, Interval
tv = TvDatafeed()

def get_data_of_all_accounts():
  pass

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



def reversing_dataFrame(data):
  data = data.iloc[::-1]
  data.reset_index(drop=True, inplace=True)
  return data



def matching_conditions(data, conditions):
  data = parsing_the_data(data)
  
  
  normal_indicators = ["PriceOpen", "PriceHigh", "PriceLow", "PriceClose", "MACD 12,26"]
  advanced_indicators = ["EMA", "RSI", "SMA"]
  
  
  
  
  if len(conditions) == 0 or conditions["conditions"][0]["indicator"] is None  or conditions["conditions"][0]["indicator2"] is None:
    return "There is no condition Skipping...."
  
  data = data.head(1)
  
  # Placing the conditions if all conditions are true
  for i in conditions["conditions"]:
    if data["indicator"] is None or data["indicator2"] is None:
      return None


    # Concatinating the indicator and length
    if i["indicator"] in advanced_indicators:
      i["indicator"] = i["indicator"]+"_"+str(i["length"])
      
    if i["indicator2"] in advanced_indicators:
      i["indicator2"] = i["indicator2"]+"_"+str(i["length2"])
      
      
    """
    Codition: Greater Than Or Equal (>=) and Equal (==) and Crosses Above
    If the indicator is constant value then we will check if the constant value is equal to the indicator value

    """

    # Greater Than Or Equal and Equal (>=)
    if i["condition"] == "Greater Than Or Equal" or i["condition"] == "Crosses Above" or i["condition"] == "Equal":
    # if the indicator is constant value
      if i["choice"] == "ConstantValue" and data.iloc[0][i["indicator"]] == i["constantValue"]:
        print("Placing Order")
        
      # if the indicator is not constant value
      elif data.iloc[0][i["indicator"]] >= data.iloc[0][i["indicator2"]]:
        print("Placing Order")
       
      """
      
      Codition:  Less Than Or Equal (<=) and Equal (==) and Crosses Below

      If the indicator is constant value then we will check if the constant value is equal to the indicator value

      """
     
    # Less Than Or Equal and Equal (<=)
    elif i["condition"] == "Crosses Below" or i["condition"] == "Less Than Or Equal" or i["condition"] == "Equal":
      
      # if the indicator is constant value
      if i["choice"] == "ConstantValue" and data.iloc[0][i["indicator"]] == i["constantValue"]:
        print("Placing Order")
        
        
      # if the indicator is not constant value
      elif data.iloc[0][i["indicator"]] <= data.iloc[0][i["indicator2"]]:
        print("Placing Order")
      
            

  
def parsing_the_data(jsonData):
  # Taking Main Values
  # binance_api = jsonData["binance_api"]
  # binance_secret = jsonData["binance_secret"]
  # discord_webhook = jsonData["discord_webhook"]
  # takeProfit = jsonData["takeProfit"]
  # stopLoss = jsonData["stopLoss"]
  
  
  data =  get_btc_data()


  neutral_indicators = ["PriceOpen", "PriceHigh", "PriceLow", "PriceClose", "MACD 12,26"]

  advanced_indicators = ["EMA", "RSI", "SMA"]
  
  all_conditions =  []


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
        
  data = reversing_dataFrame(data)
      
  return data