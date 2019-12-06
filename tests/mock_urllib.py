import re
from urllib.error import HTTPError

class MockResponse:

    def __init__(self, data):
        self.data = data

    def read(self, amt=None):
        amt = min(amt or len(self.data), len(self.data))
        part = self.data[:amt]
        self.data = self.data[amt:]
        return part

    def close(self):
        ...


def mock_urlopen(url):
    if url == 'https://api.wynncraft.com/v2/player/ValidPlayer/stats':
        return MockResponse('{"data":[{"classes":[]}]}')
    elif re.match(r'https://api\.wynncraft\.com/v2/player/.+?/stats', url):
        raise HTTPError(url, 400, 'Bad Request', None, None)
    elif url == 'https://api.wynncraft.com/public_api.php?action=onlinePlayers':
        return MockResponse('{"WC1":["Player"],"request":{"timestamp":0,"version":0}}')
    elif url == 'https://api.wynncraft.com/public_api.php?action=onlinePlayersSum':
        return MockResponse('{"players_online":1,"request":{"timestamp":0,"version":0}}')
    elif url == 'https://api.wynncraft.com/public_api.php?action=guildList':
        return MockResponse('{"guilds":["GuildName"],"request":{"timestamp":0,"version":0}}')
    elif url == 'https://api.wynncraft.com/public_api.php?action=guildStats&command=ValidGuild':
        return MockResponse('{"name":"ValidGuild","members":[{"name":"Player","rank":"OWNER"}],"request":{"timestamp":0,"version":0}}')
    elif re.match(r'https://api\.wynncraft\.com/public_api\.php\?action=guildStats&command=.+', url):
        return MockResponse('{"error":"Guild not found"}')
    elif url == 'https://api.wynncraft.com/v2/ingredient/list':
        return MockResponse('{"data":["Ingredient"]}')
    elif url == 'https://api.wynncraft.com/v2/ingredient/get/Valid_Ingredient':
        return MockResponse('{"data":[{"name":"Ingredient"}]}')
    elif re.match(r'https://api\.wynncraft\.com/v2/ingredient/get/.+', url):
        raise HTTPError(url, 400, 'Bad Request', None, None)
    elif url == 'https://api.wynncraft.com/v2/ingredient/search/name/Ingredient':
        return MockResponse('{"data":[{"name":"Ingredient"}]}')
    elif url == 'https://api.wynncraft.com/v2/ingredient/search/_/_':
        raise HTTPError(url, 400, 'Bad Request', None, None)
    elif url == 'https://api.wynncraft.com/public_api.php?action=itemDB&search=Item&category=':
        return MockResponse('{"items":[{"name":"Item"}],"request":{"timestamp":0,"version":0}}')
    elif url == 'https://api.wynncraft.com/public_api.php?action=statsLeaderboard&type=player&timeframe=alltime':
        return MockResponse('{"data":[{"name":"Player"}],"request":{"timestamp":0,"version":0}}')
    elif url == 'https://api.wynncraft.com/public_api.php?action=statsLeaderboard&type=pvp&timeframe=alltime':
        return MockResponse('{"data":[{"name":"Player"}],"request":{"timestamp":0,"version":0}}')
    elif url == 'https://api.wynncraft.com/public_api.php?action=statsLeaderboard&type=guild&timeframe=alltime':
        return MockResponse('{"data":[{"name":"Guild"}],"request":{"timestamp":0,"version":0}}')
    elif url == 'https://api.wynncraft.com/v2/recipe/get/Boots-1-3':
        return MockResponse('{"data":[{"id":"Boots-1-3"}]}')
    elif url == 'https://api.wynncraft.com/v2/recipe/get/Invalid-1-3':
        return MockResponse('{"data":[]}')
    elif re.match(r'https://api\.wynncraft\.com/v2/recipe/get/.+', url):
        raise HTTPError(url, 400, 'Bad Request', None, None)
    elif url == 'https://api.wynncraft.com/v2/recipe/list':
        return MockResponse('{"data":["Boots-1-3"]}')
    elif url == 'https://api.wynncraft.com/v2/recipe/search/_/_':
        raise HTTPError(url, 400, 'Bad Request', None, None)
    elif url == 'https://api.wynncraft.com/v2/recipe/search/type/Boots':
        return MockResponse('{"data":[{"id":"Boots-1-3"}]}')
    raise Exception('Unexpected HTTP request: {0}'.format(url))

