"""
Copyright 2020 Zakru

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

from wynn import network

from . import mock_urllib


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
