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
from urllib.error import HTTPError

from wynn import player

from .mock_urllib import MockResponse


class TestGetPlayer(TestCase):
    """Test wynn.player.get_player

    HTTP responses are mocked.
    """

    @patch('urllib.request.urlopen', side_effect=HTTPError('https://api.wynncraft.com/v2/player/InvalidPlayer/stats', 400, 'Bad Request', None, None))
    def test_get_player_with_invalid_player(self, mock_urlopen: Mock):
        """get_player with an invalid player's name returns None"""
        self.assertIsNone(player.get_player('InvalidPlayer'))
        mock_urlopen.assert_called_once_with('https://api.wynncraft.com/v2/player/InvalidPlayer/stats')

    @patch('urllib.request.urlopen', return_value=MockResponse('{"data":[{"classes":[]}]}'))
    def test_get_player_with_valid_player(self, mock_urlopen: Mock):
        """get_player with a valid player's name returns a Player"""
        self.assertIsInstance(player.get_player('ValidPlayer'), player.Player)
        mock_urlopen.assert_called_once_with('https://api.wynncraft.com/v2/player/ValidPlayer/stats')
