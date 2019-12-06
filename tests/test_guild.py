from unittest import TestCase
from unittest.mock import patch

from wynn import guild

import mock_urllib


@patch('urllib.request.urlopen', mock_urllib.mock_urlopen)
class TestGetGuilds(TestCase):
    """Test wynn.guild.get_guilds
    
    HTTP responses are mocked.
    """

    def test_get_guilds(self):
        """get_guilds returns a list"""
        self.assertIsInstance(guild.get_guilds(), list)


@patch('urllib.request.urlopen', mock_urllib.mock_urlopen)
class TestGetGuild(TestCase):
    """Test wynn.guild.get_guild
    
    HTTP responses are mocked.
    """

    def test_get_guild_with_invalid_guild(self):
        """get_guild with an invalid guild name returns None"""
        self.assertIsNone(guild.get_guild('InvalidGuild'))

    def test_get_guild_with_valid_guild(self):
        """get_guild with a valid guild name returns a Guild"""
        self.assertIsInstance(guild.get_guild('ValidGuild'), guild.Guild)
