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
