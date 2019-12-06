from unittest import TestCase
from unittest.mock import patch

from wynn import player

import mock_urllib


@patch('urllib.request.urlopen', mock_urllib.mock_urlopen)
class TestGetPlayer(TestCase):
    """Test wynn.player.get_player
    
    HTTP responses are mocked.
    """

    def test_get_player_with_invalid_player(self):
        """get_player with an invalid player's name returns None"""
        self.assertIsNone(player.get_player('InvalidPlayer'))

    def test_get_player_with_valid_player(self):
        """get_player with a valid player's name returns a Player"""
        self.assertIsInstance(player.get_player('ValidPlayer'), player.Player)
