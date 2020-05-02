import yfinance as yf
import pandas as pd
#newsapi d04c306a8941438eaeb5db7618483935
import nltk
from nltk.corpus import stopwords
import re, pprint
import requests
import ast
from bs4 import BeautifulSoup


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

    # stock_data = {}
    # print(data.recommendations)
    # try:
    #     for x in data.info:
    #         print(x, ":", data.info[x])
    #     hist = data.history(period="5d")
    #     print(hist)
    # except Exception as e:
    #     print(e)

def keyword_search(stock):
    data = yf.Ticker(stock)
    # summary = data.info["longBusinessSummary"]
    # sr = stopwords.words('english')
    # text = [t.lower() for t in summary.split()]
    regex = re.compile("[^a-zA-Z]")
    # for x in range(0, len(text)):
    #     text[x] = regex.sub('', text[x])
    # clean_text = text[:]
    # for token in text:
    #     if token in sr:
    #         clean_text.remove(token)
    #     elif token == '':
    #         clean_text.remove(token)
    # freq = nltk.FreqDist(clean_text)
    # print(nltk.pos_tag(list(set(clean_text))))
    # print(nltk.word_tokenize(' '.join(clean_text)))
    # print(freq)
    #
    # sentences = nltk.sent_tokenize(data.info["longBusinessSummary"])
    # sentences = [nltk.word_tokenize(sent) for sent in sentences]
    # sentences = [nltk.pos_tag(sent) for sent in sentences]
    # print(sentences)
    # grammar = "NP: {<DT>?<JJ>*<NN>}"[2]
    #
    # for sentence in sentences:
    #     cp = nltk.RegexpParser(grammar)
    #     result = cp.parse(sentence)
    #     print(result)
    sector = data.info["sector"]

    industry = data.info["industry"]
    longname = data.info["longName"]
    symbol = data.info["symbol"]
    market = data.info["market"]

    search_query = [sector + " stocks", industry + " stocks", symbol, market]

    try:
        search = longname.split( )
        new_search = []
        for x in search:
            print(re.match('^[a-zA-Z]+$', x))
            if re.match('^[a-zA-Z]+$', x):
                new_search.append(x)

        search = ' '.join(new_search)
        search_query.append(search)

        for x in range(0, len(search_query)):
            search_query[x] = regex.sub(' ', search_query[x])

        print(search_query)

        url = ("https://newsapi.org/v2/everything?q={}&sortBy=popularity&pageSize=3&apiKey=d04c306a8941438eaeb5db7618483935".format(search_query[0]))
        response = requests.get(url)
        print(response.json())
        response.raise_for_status()
    except Exception as e:
        raise e
        #print("Error!")


def test():
    nltk.download()

look_up("MSFT")
keyword_search("MSFT")