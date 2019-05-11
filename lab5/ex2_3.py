import requests as req
import numpy as np
from time import sleep


class User:
    """Stores ids, usernames, first and last names of users"""

    def __init__(self, uid, nick, first, last):
        self.id = uid
        self.username = nick
        self.name = first + ' ' + last
        self.btc = np.round(np.abs(np.random.randn()), 8)
        self.pln = np.random.randint(10000, 20000)


def transaction(user1, user2):
    resp = req.get("https://bitbay.net/API/Public/BTCPLN/ticker.json")
    market_data = resp.json()
    bid = market_data['bid']

    trans_btc = np.round(np.abs(np.random.randn()), 8)
    price = np.round(bid * trans_btc, 2)
    if user1.btc < trans_btc or user2.pln < price:
        return 0
    else:
        user1.btc -= trans_btc
        user2.btc += trans_btc
        user1.pln += price
        user2.pln -= price

    print('transaction #{}: {} exchanged {:.8f} BTC with {} for {:.2f} PLN'.format(n+1, user1.username, trans_btc,
                                                                                   user2.username, price))
    print('{} after transaction: {:.8f} BTC, {:.2f} PLN'.format(user1.username, user1.btc, user1.pln))
    print('{} after transaction: {:.8f} BTC, {:.2f} PLN\n'.format(user2.username, user2.btc, user2.pln))

    return 1


response = req.get('https://randomuser.me/api/?results=100')
data = response.json()
user_data = data['results']

users = []
for i in range(len(user_data)):
    users.append(User(user_data[i]['login']['uuid'], user_data[i]['login']['username'], user_data[i]['name']['first'],
                      user_data[i]['name']['last']))

n = 0
while n < 100:
    u = np.random.randint(0, 100, 2)
    if u[0] == u[1]:
        u[0] += 1

    try:
        n += transaction(users[u[0]], users[u[1]])
    except IndexError:
        u[0] -= 2
        n += transaction(users[u[0]], users[u[1]])
    sleep(0.03)
