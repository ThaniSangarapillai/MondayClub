import yfinance as yf
import pandas as pd
#newsapi d04c306a8941438eaeb5db7618483935
import nltk
from nltk.corpus import stopwords
import re, pprint
import requests
import ast
from bs4 import BeautifulSoup
import pickle
import string
from nltk.tag import pos_tag
from nltk.stem.wordnet import WordNetLemmatizer
from nltk import FreqDist
from nltk import classify
from nltk import NaiveBayesClassifier
import random
import json
from .models import Stock

def read_ticker_json():
    with open("ticker.json") as f:
        data = json.load(f)
    count = 0
    for x in data:
        print(count)
        data = yf.Ticker(x['Symbol'])
        try:
            original = data.info
            stock = Stock(ticker=x["Symbol"], company_name=x["Company Name"], price=original["regularMarketPrice"])
            stock.save()
        except:
            pass

        count += 1

def readtickerdata(stock):
    data = yf.Ticker(stock)

    try:
        original = data.info
        # White list picks the values we want to KEEP from the original data.info
        white_list = {'symbol', 'longName', 'regularMarketPrice'}

        return {k: v for k, v in original.items() if k in white_list}
    except Exception:
        return False

def look_up(stock, total_time="5d", interval_time="1d"):

    data = yf.Ticker(stock)

    original = data.info
    print(data.info)
    #White list picks the values we want to KEEP from the original data.info
    white_list = {"sector", "fullTimeEmployees", "longBusinessSummary", "city", "phone",
                  "state", "country", "website", "address1", "industry",
                  "currency", "marketCap", "sharesOutstanding", "bookValue", "logo_url", 'regularMarketPrice'}

    returnDict = {k:v for k,v in original.items() if k in white_list}

    #Creates a dictionary that contains numerical information like open/close/volume for specific dates of the time
    hist = data.history(period=total_time,interval = interval_time)
    #hist['Date'] = hist['Date'].astype('string')
    temp_list = list()
    for i, x in hist.iterrows():
        temp_list.append(str(i))
    hist['Datetime'] = temp_list
    hist = hist.set_index('Datetime', drop=True)
    hist = hist.to_dict()
    print(hist)
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
    stop_words = stopwords.words('english')
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
    news_sentiment = []
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
        #need to add for loop here, remind
        url = ("https://newsapi.org/v2/everything?q={}&sortBy=popularity&pageSize=3&apiKey=d04c306a8941438eaeb5db7618483935".format(search_query[0]))
        response = requests.get(url)
        print(response.json())
        response.raise_for_status()
        news = response.json()
        for x in news['articles']:
            with open('my_classifier.pickle', 'rb') as f:
                classifier = pickle.load(f)
                string_input = x["description"]
                title = []
                title_nontrunc = string_input.split(" ")
                for y in range(0, len(list(title_nontrunc))):
                    if title_nontrunc[y] != '':
                        title.append(title_nontrunc[y].lower())
                title = lemmatize_sentence(title, stop_words)
                result = classifier.classify(dict([token, True] for token in title))
                print(result)

            news_sentiment.append({"source":x["source"]["name"],
                                   "author":x["author"],
                                   "title":x["title"],
                                   "description":x["description"],
                                   "url":x["url"],
                                   "image":x["urlToImage"],
                                   "content":x["content"],
                                   "publishdate": x["publishedAt"],
                                   "sentiment":result})

        return news_sentiment

    except Exception as e:
        raise e
        #print("Error!")


def test():
    nltk.download()
#

def lemmatize_sentence(tokens, stop_words):
    cleaned = []
    lemmatizer = WordNetLemmatizer()
    lemmatized_sentence = []
    for token, tag in pos_tag(tokens):
        token = token.strip(string.punctuation)
        token = re.sub("^[0-9]-.+", '', token)
        token = re.sub("^[0-9]+$", '', token)
        #print(string.punctuation

        pos = ''
        if tag.startswith('NN'):
            pos = 'n'
        elif tag.startswith('VB'):
            pos = 'v'
        else:
            pos = 'a'

        token = lemmatizer.lemmatize(token, pos)

        if len(token) > 0 and token not in string.punctuation and token.lower() not in stop_words:
            cleaned.append(token.lower())
    return cleaned


print(look_up("WEF.TO"))
# read_ticker_json()
# # keyword_search("MSFT")