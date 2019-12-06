from unittest import TestCase
from unittest.mock import patch

from wynn import item

import mock_urllib


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
