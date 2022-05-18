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

from wynn import item

from .mock_urllib import MockResponse


class TestSearchItem(TestCase):
    """Test wynn.item.search_item

    HTTP responses are mocked.
    """

    def test_search_item_with_no_args(self):
        """
        search_item with no arguments raises a TypeError
        """
        with self.assertRaises(TypeError):
            item.search_item()

    def test_search_item_with_empty_args(self):
        """
        search_item with empty arguments raises a TypeError
        """
        with self.assertRaises(TypeError):
            item.search_item(name='', category='')

    @patch('urllib.request.urlopen', return_value=MockResponse('{"items":[{"name":"Item"}],"request":{"timestamp":0,"version":0}}'))
    def test_search_item_with_args(self, mock_urlopen: Mock):
        """
        search_item with arguments returns a list
        """
        self.assertIsInstance(item.search_item(name='Item'), list)
        mock_urlopen.assert_called_once_with('https://api.wynncraft.com/public_api.php?action=itemDB&search=Item&category=')
