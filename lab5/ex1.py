import requests as req
from numpy import argmin, argmax

bitbay = req.get("https://bitbay.net/API/Public/BTCPLN/ticker.json")
bitmarket = req.get("https://www.bitmarket.pl/json/BTCPLN/ticker.json")
bitbay_data = bitbay.json()
bitmarket_data = bitmarket.json()

markets = ['Bitbay', 'Bitmarket']
sell = [bitbay_data['bid'], bitmarket_data['bid']]
buy = [bitbay_data['ask'], bitmarket_data['ask']]

ind_sell = int(argmax(sell))
ind_buy = int(argmin(buy))
best_sell = markets[ind_sell]
best_buy = markets[ind_buy]

print('Currently {} is better for buying, while {} is better for selling'.format(best_buy, best_sell))
