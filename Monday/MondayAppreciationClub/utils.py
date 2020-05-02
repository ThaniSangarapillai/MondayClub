import yfinance as yf
import pandas as pd

def look_up(stock,total_time = "5d",interval_time = "1d"):

    data = yf.Ticker(stock)

    original = data.info
    #White list picks the values we want to KEEP from the original data.info
    white_list = {"sector", "fullTimeEmployees", "longBusinessSummary", "city", "phone",
                  "state", "country", "website", "address1", "industry",
                  "currency", "marketCap", "sharesOutstanding", "bookValue", "logo_url"}

    returnDict = {k:v for k,v in original.items() if k in white_list}

    #Creates a dictionary that contains numerical information like open/close/volume for specific dates of the time
    hist = data.history(period=total_time,interval = interval_time).to_dict()

    #Combines both dictionaries into one
    returnDict.update(hist)

    return returnDict
