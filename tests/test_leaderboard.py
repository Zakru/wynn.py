from unittest import TestCase
from unittest.mock import patch

from wynn import leaderboard

import mock_urllib


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
