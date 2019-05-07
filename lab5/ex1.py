import requests as req

bitbay = req.get("https://bitbay.net/API/Public/BTCPLN/ticker.json")
bitmarket = req.get("https://www.bitmarket.pl/json/BTCPLN/ticker.json")
bitbay_data = bitbay.json()
bitmarket_data = bitmarket.json()

if bitbay_data['bid'] > bitmarket_data['bid']:
    print('Bitbay is better for selling')
elif bitbay_data['bid'] < bitmarket_data['bid']:
    print('Bitmarket is better for selling')
else:
    print('Markets have the same selling')

if bitbay_data['ask'] > bitmarket_data['ask']:
    print('Bitmarket is better for buying')
elif bitbay_data['ask'] < bitmarket_data['ask']:
    print('Bitbay is better for buying')
else:
    print('Markets have the same buying price')
