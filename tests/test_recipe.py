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

from wynn import recipe
from wynn.requests import ObjectFromDict

from .mock_urllib import MockResponse


class TestGetRecipe(TestCase):
    """Test wynn.recipe.get_recipe

    HTTP responses are mocked.
    """

    @patch('urllib.request.urlopen', side_effect=HTTPError('https://api.wynncraft.com/v2/recipe/get/InvalidRecipeID', 400, 'Bad Request', None, None))
    def test_get_recipe_with_invalid_id(self, mock_urlopen: Mock):
        """
        get_recipe with an invalid recipe ID returns None
        """
        self.assertIsNone(recipe.get_recipe('InvalidRecipeID'))
        mock_urlopen.assert_called_once_with('https://api.wynncraft.com/v2/recipe/get/InvalidRecipeID')

    @patch('urllib.request.urlopen', return_value=MockResponse('{"data":[]}'))
    def test_get_recipe_with_invalid_id_valid_format(self, mock_urlopen: Mock):
        """
        get_recipe with an invalid recipe ID but in the correct format
        returns None
        """
        self.assertIsNone(recipe.get_recipe('Invalid-1-3'))
        mock_urlopen.assert_called_once_with('https://api.wynncraft.com/v2/recipe/get/Invalid-1-3')

    @patch('urllib.request.urlopen', return_value=MockResponse('{"data":[{"id":"Boots-1-3"}]}'))
    def test_get_recipe_with_valid_id(self, mock_urlopen: Mock):
        """
        get_recipe with a valid recipe ID returns an ObjectFromDict
        """
        self.assertIsInstance(recipe.get_recipe('Boots-1-3'), ObjectFromDict)
        mock_urlopen.assert_called_once_with('https://api.wynncraft.com/v2/recipe/get/Boots-1-3')


class TestGetRecipeIDs(TestCase):
    """Test wynn.recipe.get_recipe_ids

    HTTP responses are mocked.
    """

    @patch('urllib.request.urlopen', return_value=MockResponse('{"data":["Boots-1-3"]}'))
    def test_get_recipe_ids(self, mock_urlopen: Mock):
        """
        get_recipe_ids returns the recipe IDs
        """
        self.assertEqual(recipe.get_recipe_ids(), ['Boots-1-3'])
        mock_urlopen.assert_called_once_with('https://api.wynncraft.com/v2/recipe/list')


class TestSearchRecipes(TestCase):
    """Test wynn.recipe.search_recipes

    HTTP responses are mocked.
    """

    @patch('urllib.request.urlopen', side_effect=HTTPError('https://api.wynncraft.com/v2/recipe/search/_/_', 400, 'Bad Request', None, None))
    def test_search_recipes_with_invalid_query(self, mock_urlopen: Mock):
        """
        search_recipes with an invalid query returns an empty list
        """
        result = recipe.search_recipes('_', '_')
        self.assertEqual(result, [])
        mock_urlopen.assert_called_once_with('https://api.wynncraft.com/v2/recipe/search/_/_')

    @patch('urllib.request.urlopen', return_value=MockResponse('{"data":[{"id":"Boots-1-3"}]}'))
    def test_search_recipes_with_valid_query(self, mock_urlopen: Mock):
        """
        search_recipes with a valid query with results returns a
        non-empty list
        """
        result = recipe.search_recipes('type', 'Boots')
        self.assertIsInstance(result, list)
        self.assertTrue(result)
        mock_urlopen.assert_called_once_with('https://api.wynncraft.com/v2/recipe/search/type/Boots')
