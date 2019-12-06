from unittest import TestCase
from unittest.mock import patch

from wynn import territory

import mock_urllib


@patch('urllib.request.urlopen', mock_urllib.mock_urlopen)
class TestGetTerritories(TestCase):
    """Test wynn.territory.get_territories
    
    HTTP responses are mocked.
    """

    def test_get_territories(self):
        """
        get_territories returns a list
        """
        self.assertIsInstance(territory.get_territories(), list)
