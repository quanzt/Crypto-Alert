from binance.client import Client
import json
import time

client = Client('api_key', 'api_secret')

def create_tuples():
    """Return a list of tuples with USDT trading pairs
    (symbol, price)
    """
    ret = client.get_all_tickers()
    ret = [x for x in ret if x['symbol'].endswith('USDT')]
    ret = [(x['symbol'][:-4], round(float(x['price']), 4)) for x in ret]
    return ret

def price_only():
    """Return a 2D list of prices
    [[btcprice], [ethprice], ...]
    """
    ret = client.get_all_tickers()
    ret = [x for x in ret if x['symbol'].endswith('USDT')]
    ret = [[round(float(x['price']), 4)] for x in ret]
    return ret

def yesterday_price(symbol='BTCUSDT'):
    yesterday = client.get_historical_klines(symbol, Client.KLINE_INTERVAL_1MINUTE, "1 day ago UTC")[0]
    return yesterday[4]

if __name__ == '__main__':
    # print (yesterday_price('BCCUSDT'))
    create_tuples()

