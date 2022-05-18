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

from wynn import search
from wynn.requests import ObjectFromDict, DictObjectList

from .mock_urllib import MockResponse


class TestSearch(TestCase):
    """Test wynn.search.search

    HTTP responses are mocked.
    """

    @patch('urllib.request.urlopen', return_value=MockResponse('{"error":"Search required"}'))
    def test_search_with_empty_arg(self, mock_urlopen: Mock):
        """
        search with an empty argument returns empty DictObjectLists
        """
        result = search.search('')
        self.assertIsInstance(result, ObjectFromDict)
        self.assertIsInstance(result.guilds, DictObjectList)
        self.assertFalse(result.guilds)
        self.assertIsInstance(result.players, DictObjectList)
        self.assertFalse(result.players)
        mock_urlopen.assert_called_once_with('https://api.wynncraft.com/public_api.php?action=statsSearch&search=')

    @patch('urllib.request.urlopen', return_value=MockResponse('{"guilds":["GuildName"],"players":["PlayerName"],"request":{"timestamp":0,"version":0}}'))
    def test_search_with_non_empty_arg(self, mock_urlopen: Mock):
        """
        search with a non-empty argument returns DictObjectLists
        """
        result = search.search('Name')
        self.assertIsInstance(result, ObjectFromDict)
        self.assertIsInstance(result.guilds, DictObjectList)
        self.assertIsInstance(result.players, DictObjectList)
        mock_urlopen.assert_called_once_with('https://api.wynncraft.com/public_api.php?action=statsSearch&search=Name')
