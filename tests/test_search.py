from unittest import TestCase
from unittest.mock import patch

from wynn import search
from wynn.requests import ObjectFromDict

import mock_urllib


@patch('urllib.request.urlopen', mock_urllib.mock_urlopen)
class TestSearch(TestCase):
    """Test wynn.search.search
    
    HTTP responses are mocked.
    """

    def test_search_with_empty_arg(self):
        """
        search with an empty argument returns empty lists
        """
        result = search.search('')
        self.assertIsInstance(result, ObjectFromDict)
        self.assertIsInstance(result.guilds, list)
        self.assertFalse(result.guilds)
        self.assertIsInstance(result.players, list)
        self.assertFalse(result.players)

    def test_search_with_non_empty_arg(self):
        """
        search with a non-empty argument returns lists
        """
        result = search.search('Name')
        self.assertIsInstance(result, ObjectFromDict)
        self.assertIsInstance(result.guilds, list)
        self.assertIsInstance(result.players, list)
