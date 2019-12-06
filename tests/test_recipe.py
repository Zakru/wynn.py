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

from wynn import recipe
from wynn.requests import ObjectFromDict

import mock_urllib


@patch('urllib.request.urlopen', mock_urllib.mock_urlopen)
class TestGetRecipe(TestCase):
    """Test wynn.recipe.get_recipe
    
    HTTP responses are mocked.
    """

    def test_get_recipe_with_invalid_id(self):
        """
        get_recipe with an invalid recipe ID returns None
        """
        self.assertIsNone(recipe.get_recipe('InvalidRecipeID'))

    def test_get_recipe_with_invalid_id_valid_format(self):
        """
        get_recipe with an invalid recipe ID but in the correct format
        returns None
        """
        self.assertIsNone(recipe.get_recipe('Invalid-1-3'))

    def test_get_recipe_with_valid_id(self):
        """
        get_recipe with a valid recipe ID returns an ObjectFromDict
        """
        self.assertIsInstance(recipe.get_recipe('Boots-1-3'), ObjectFromDict)


@patch('urllib.request.urlopen', mock_urllib.mock_urlopen)
class TestGetRecipeIDs(TestCase):
    """Test wynn.recipe.get_recipe_ids
    
    HTTP responses are mocked.
    """

    def test_get_recipe_ids(self):
        """
        get_recipe_ids returns a list
        """
        self.assertIsInstance(recipe.get_recipe_ids(), list)


@patch('urllib.request.urlopen', mock_urllib.mock_urlopen)
class TestSearchRecipes(TestCase):
    """Test wynn.recipe.search_recipes
    
    HTTP responses are mocked.
    """

    def test_search_recipes_with_invalid_query(self):
        """
        search_recipes with an invalid query returns an empty list
        """
        result = recipe.search_recipes('_', '_')
        self.assertIsInstance(result, list)
        self.assertFalse(result)

    def test_search_recipes_with_valid_query(self):
        """
        search_recipes with a valid query with results returns a
        non-empty list
        """
        result = recipe.search_recipes('type', 'Boots')
        self.assertIsInstance(result, list)
        self.assertTrue(result)
