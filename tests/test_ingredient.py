from unittest import TestCase
from unittest.mock import patch

from wynn import ingredient
from wynn.requests import ObjectFromDict

import mock_urllib


@patch('urllib.request.urlopen', mock_urllib.mock_urlopen)
class TestGetIngredientNames(TestCase):
    """Test wynn.ingredient.get_ingredient_names
    
    HTTP responses are mocked.
    """

    def test_get_ingredient_names(self):
        """
        get_ingredient_names returns a list
        """
        self.assertIsInstance(ingredient.get_ingredient_names(), list)


@patch('urllib.request.urlopen', mock_urllib.mock_urlopen)
class TestGetIngredient(TestCase):
    """Test wynn.ingredient.get_ingredient
    
    HTTP responses are mocked.
    """

    def test_get_ingredient_with_invalid_ingredient(self):
        """
        get_ingredient with an invalid ingredient returns None
        """
        self.assertIsNone(ingredient.get_ingredient('Invalid Ingredient'))

    def test_get_ingredient_with_valid_ingredient(self):
        """
        get_ingredient with a valid ingredient returns an
        ObjectFromDict
        """
        self.assertIsInstance(ingredient.get_ingredient('Valid Ingredient'), ObjectFromDict)


@patch('urllib.request.urlopen', mock_urllib.mock_urlopen)
class TestSearchIngredients(TestCase):
    """Test wynn.ingredient.search_ingredients
    
    HTTP responses are mocked.
    """

    def test_search_ingredients_with_invalid_query(self):
        """
        search_ingredients with an invalid query returns an empty
        list
        """
        result = ingredient.search_ingredients('_', '_')
        self.assertIsInstance(result, list)
        self.assertFalse(result)

    def test_search_ingredients_with_valid_query(self):
        """
        search_ingredients with a valid query with results returns a
        non-empty list
        """
        result = ingredient.search_ingredients('name', 'Ingredient')
        self.assertIsInstance(result, list)
        self.assertTrue(result)