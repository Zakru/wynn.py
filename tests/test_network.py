from unittest import TestCase
from unittest.mock import patch

from wynn import network

import mock_urllib


@patch('urllib.request.urlopen', mock_urllib.mock_urlopen)
class TestGetServers(TestCase):
    """Test wynn.network.get_servers
    
    HTTP responses are mocked.
    """

    def test_get_servers(self):
        """get_servers returns a dict"""
        self.assertIsInstance(network.get_servers(), dict)


@patch('urllib.request.urlopen', mock_urllib.mock_urlopen)
class TestGetPlayerSum(TestCase):
    """Test wynn.network.get_player_sum
    
    HTTP responses are mocked.
    """

    def test_get_player_sum(self):
        """get_player_sum returns an int"""
        self.assertIsInstance(network.get_player_sum(), int)
