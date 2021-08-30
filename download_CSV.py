import pandas as pd
from binance.client import Client
import datetime as dt


# client configuration
api_key = '' 
api_secret = ''
client = Client(api_key, api_secret) 

symbol = "DOTUSDT"
interval = Client.KLINE_INTERVAL_15MINUTE

klines = client.get_historical_klines(symbol, interval, "1 Jan,2021")
df = pd.DataFrame(klines)

# create colums name
df.columns = ['open_time',
            'open', 'high', 'low', 'close', 'volume',
            'close_time', 'qav', 'num_trades',
            'taker_base_vol', 'taker_quote_vol', 'ignore']
            
# change the timestamp
df.index = [dt.datetime.fromtimestamp(x/1000.0) for x in df.close_time]
df.to_csv(symbol+interval+'.csv', index = None, header=True)

