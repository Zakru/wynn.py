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

from wynn import guild

from .mock_urllib import MockResponse


class TestGetGuilds(TestCase):
    """Test wynn.guild.get_guilds

    HTTP responses are mocked.
    """

    @patch('urllib.request.urlopen', return_value=MockResponse('{"guilds":["GuildName"],"request":{"timestamp":0,"version":0}}'))
    def test_get_guilds(self, mock_urlopen: Mock):
        """get_guilds returns the guilds"""
        self.assertEqual(guild.get_guilds(), ["GuildName"])
        mock_urlopen.assert_called_once_with('https://api.wynncraft.com/public_api.php?action=guildList')


class TestGetGuild(TestCase):
    """Test wynn.guild.get_guild

    HTTP responses are mocked.
    """

    @patch('urllib.request.urlopen', return_value=MockResponse('{"error":"Guild not found"}'))
    def test_get_guild_with_invalid_guild(self, mock_urlopen: Mock):
        """get_guild with an invalid guild name returns None"""
        self.assertIsNone(guild.get_guild('InvalidGuild'))
        mock_urlopen.assert_called_once_with('https://api.wynncraft.com/public_api.php?action=guildStats&command=InvalidGuild')

    @patch('urllib.request.urlopen', return_value=MockResponse('{"name":"ValidGuild","members":[{"name":"Player","rank":"OWNER"}],"request":{"timestamp":0,"version":0}}'))
    def test_get_guild_with_valid_guild(self, mock_urlopen: Mock):
        """get_guild with a valid guild name returns a Guild"""
        self.assertIsInstance(guild.get_guild('ValidGuild'), guild.Guild)
        mock_urlopen.assert_called_once_with('https://api.wynncraft.com/public_api.php?action=guildStats&command=ValidGuild')
