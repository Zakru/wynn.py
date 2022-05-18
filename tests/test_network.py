"""
Copyright 2020-2022 Zakru

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files
(the "Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be included
in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

from unittest import TestCase
from unittest.mock import Mock, patch

from wynn import network

from .mock_urllib import MockResponse


class TestGetServers(TestCase):
    """Test wynn.network.get_servers

    HTTP responses are mocked.
    """

    @patch('urllib.request.urlopen', return_value=MockResponse('{"WC1":["Player"],"request":{"timestamp":0,"version":0}}'))
    def test_get_servers(self, mock_urlopen: Mock):
        """get_servers returns correct data as a dict"""
        self.assertEqual(network.get_servers(), {"WC1": ["Player"]})
        mock_urlopen.assert_called_once_with('https://api.wynncraft.com/public_api.php?action=onlinePlayers')


class TestGetPlayerSum(TestCase):
    """Test wynn.network.get_player_sum

    HTTP responses are mocked.
    """

    @patch('urllib.request.urlopen', return_value=MockResponse('{"players_online":1,"request":{"timestamp":0,"version":0}}'))
    def test_get_player_sum(self, mock_urlopen: Mock):
        """get_player_sum returns the player count"""
        self.assertEqual(network.get_player_sum(), 1)
        mock_urlopen.assert_called_once_with('https://api.wynncraft.com/public_api.php?action=onlinePlayersSum')
