"""
Copyright 2019 Zakru

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
from unittest.mock import patch

from wynn import leaderboard

from . import mock_urllib


@patch('urllib.request.urlopen', mock_urllib.mock_urlopen)
class TestGetPlayerLeaderboard(TestCase):
    """Test wynn.leaderboard.get_player_leaderboard
    
    HTTP responses are mocked.
    """

    def test_get_player_leaderboard(self):
        """
        get_player_leaderboard returns a list
        """
        self.assertIsInstance(leaderboard.get_player_leaderboard(), list)


@patch('urllib.request.urlopen', mock_urllib.mock_urlopen)
class TestGetPVPLeaderboard(TestCase):
    """Test wynn.leaderboard.get_pvp_leaderboard
    
    HTTP responses are mocked.
    """

    def test_get_pvp_leaderboard(self):
        """
        get_pvp_leaderboard returns a list
        """
        self.assertIsInstance(leaderboard.get_pvp_leaderboard(), list)


@patch('urllib.request.urlopen', mock_urllib.mock_urlopen)
class TestGetGuildLeaderboard(TestCase):
    """Test wynn.leaderboard.get_guild_leaderboard
    
    HTTP responses are mocked.
    """

    def test_get_guild_leaderboard(self):
        """
        get_guild_leaderboard returns a list
        """
        self.assertIsInstance(leaderboard.get_guild_leaderboard(), list)
