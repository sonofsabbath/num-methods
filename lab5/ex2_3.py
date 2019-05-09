import requests as req


class User:
    """Stores ids, usernames, first and last names of users"""

    def __init__(self, uid, nick, first, last):
        self.id = uid
        self.username = nick
        self.name = first + ' ' + last


response = req.get('https://randomuser.me/api/?results=100')
data = response.json()
user_data = data['results']

users = []
for i in range(len(user_data)):
    users.append(User(user_data[i]['login']['uuid'], user_data[i]['login']['username'], user_data[i]['name']['first'],
                      user_data[i]['name']['last']))
