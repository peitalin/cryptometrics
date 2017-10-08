
import pandas as pd
import seaborn as sb
import requests
from requests import get
from datetime import datetime
import pickle



version = 'v1.1'
api_endpoint_markets = "https://bittrex.com/api/v1.1/public/getmarkets"

def getPrices(ticker):
    """ ticker: coin ticker """
    url = "https://bittrex.com/api/v1.1/public/getmarkethistory?market={}".format(ticker)
    res = requests.get(url)
    return res.json()

print(getPrices('ETH-NMR'))
omg = pd.DataFrame(getPrices('ETH-OMG')['result'])


