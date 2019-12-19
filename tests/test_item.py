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

from wynn import item

from . import mock_urllib


@patch('urllib.request.urlopen', mock_urllib.mock_urlopen)
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

    def test_search_item_with_args(self):
        """
        search_item with arguments returns a list
        """
        self.assertIsInstance(item.search_item(name='Item'), list)
