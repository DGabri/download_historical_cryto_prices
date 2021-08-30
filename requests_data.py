import requests
import json
import pandas as pd
import datetime as dt

def get_klines(symbol, interval, start, end):
    url = 'https://api.binance.com/api/v3/klines'
    start = str(int(start.timestamp()*1000))
    end = str(int(end.timestamp()*1000))
    limit = 1000
    par = {'symbol': symbol, 'interval': interval, 'startTime': start, 'endTime': end, 'limit': limit}
    klines = pd.DataFrame(json.loads(requests.get(url, params= par).text))
    klines = klines.iloc[:, 0:11] 
    klines.columns = ['datetime', 'o', 'h', 'l', 'c', 'volume','close_time', 'qav', 'num_trades',
            'taker_base_vol', 'taker_quote_vol']
    klines.index = [dt.datetime.fromtimestamp(x/1000.0) for x in klines.datetime]
    return klines

data = get_klines('DOTUSDT', '30m', dt.datetime(2021,5,1), dt.datetime(2021,8,1))
data.to_csv('dotusdt30m')
