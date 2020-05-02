import yfinance as yf
import pandas as pd

def look_up(stock):
    data = yf.Ticker(stock)
    print(data.info)
    hist = data.history(period="5d")
    print(hist)

look_up("WEF.TO")
