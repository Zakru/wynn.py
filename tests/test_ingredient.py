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

from wynn import ingredient
from wynn.requests import ObjectFromDict

from .mock_urllib import MockResponse


class TestGetIngredientNames(TestCase):
    """Test wynn.ingredient.get_ingredient_names

    HTTP responses are mocked.
    """

    @patch('urllib.request.urlopen', return_value=MockResponse('{"data":["Ingredient", "Another"]}'))
    def test_get_ingredient_names(self, mock_urlopen: Mock):
        """
        get_ingredient_names returns the ingredients
        """
        self.assertEqual(ingredient.get_ingredient_names(), ["Ingredient", "Another"])
        mock_urlopen.assert_called_once_with('https://api.wynncraft.com/v2/ingredient/list')


class TestGetIngredient(TestCase):
    """Test wynn.ingredient.get_ingredient

    HTTP responses are mocked.
    """

    @patch('urllib.request.urlopen', side_effect=HTTPError('https://api.wynncraft.com/v2/ingredient/get/Invalid_Ingredient', 400, 'Bad Request', None, None))
    def test_get_ingredient_with_invalid_ingredient(self, mock_urlopen: Mock):
        """
        get_ingredient with an invalid ingredient returns None
        """
        self.assertIsNone(ingredient.get_ingredient('Invalid Ingredient'))
        mock_urlopen.assert_called_once_with('https://api.wynncraft.com/v2/ingredient/get/Invalid_Ingredient')

    @patch('urllib.request.urlopen', return_value=MockResponse('{"data":[{"name":"Ingredient"}]}'))
    def test_get_ingredient_with_valid_ingredient(self, mock_urlopen: Mock):
        """
        get_ingredient with a valid ingredient returns an
        ObjectFromDict
        """
        self.assertIsInstance(ingredient.get_ingredient('Valid Ingredient'), ObjectFromDict)
        mock_urlopen.assert_called_once_with('https://api.wynncraft.com/v2/ingredient/get/Valid_Ingredient')


class TestSearchIngredients(TestCase):
    """Test wynn.ingredient.search_ingredients

    HTTP responses are mocked.
    """

    @patch('urllib.request.urlopen', side_effect=HTTPError('https://api.wynncraft.com/v2/ingredient/search/_/_', 400, 'Bad Request', None, None))
    def test_search_ingredients_with_invalid_query(self, mock_urlopen: Mock):
        """
        search_ingredients with an invalid query returns an empty
        list
        """
        result = ingredient.search_ingredients('_', '_')
        self.assertIsInstance(result, list)
        self.assertFalse(result)
        mock_urlopen.assert_called_once_with('https://api.wynncraft.com/v2/ingredient/search/_/_')

    @patch('urllib.request.urlopen', return_value=MockResponse('{"data":[{"name":"Ingredient"}]}'))
    def test_search_ingredients_with_valid_query(self, mock_urlopen: Mock):
        """
        search_ingredients with a valid query returns a list
        """
        result = ingredient.search_ingredients('name', 'Ingredient')
        self.assertIsInstance(result, list)
        mock_urlopen.assert_called_once_with('https://api.wynncraft.com/v2/ingredient/search/name/Ingredient')