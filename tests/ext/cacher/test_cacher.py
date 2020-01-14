from unittest import TestCase
from unittest.mock import patch
from io import BytesIO

from wynn.requests import ObjectFromDict
from wynn.ext import cacher
from ... import mock_urllib


class TestCaching(TestCase):
    """Test the caching functionality"""

    def setUp(self):
        self.full_cacher = cacher.WynnCacher()
        self.full_cacher.cache = {
            'ingredient': {
                'Ingredient': ObjectFromDict({
                    'name': 'Ingredient',
                }),
            },
        }

        self.empty_cacher = cacher.WynnCacher()

        self.incomplete_cacher = cacher.WynnCacher()
        self.incomplete_cacher.cache = {}

    def test_cache_uncache(self):
        """
        Can save and load the cache
        """
        file = BytesIO()
        self.full_cacher.save_cache(file)
        file.seek(0)
        self.empty_cacher.load_cache(file)
        self.assertEqual(self.empty_cacher.cache['ingredient']['Ingredient'].name, 'Ingredient')

    def test_empty_cacher_has_key(self):
        """
        Empty cacher has subcache initialized
        """
        self.assertIn('ingredient', self.empty_cacher.cache)

    def test_load_cache_initializes_missing(self):
        """
        load_cache initializes missing subcaches
        """
        file = BytesIO()
        self.incomplete_cacher.save_cache(file)
        file.seek(0)
        self.empty_cacher.load_cache(file)
        self.assertIn('ingredient', self.empty_cacher.cache)


class TestInAny(TestCase):
    """Test the utility function _in_any"""

    def setUp(self):
        self.in_a_sequence = 'o'
        self.not_in_a_sequence = 'y'
        self.sequences = [
            'foo',
            'bar',
        ]
        self.cacher = cacher.WynnCacher()

    def test_true(self):
        """
        _in_any returns True when the item is found in a sequence
        """
        self.assertTrue(self.cacher._in_any(self.in_a_sequence, self.sequences))

    def test_false(self):
        """
        _in_any returns False when the item is not found in any sequence
        """
        self.assertFalse(self.cacher._in_any(self.not_in_a_sequence, self.sequences))


class TestAnyInAny(TestCase):
    """Test the utility function _any_in_any"""

    def setUp(self):
        self.in_a_sequence = ['x', 'a']
        self.not_in_a_sequence = ['z', 't']
        self.sequences = [
            'foo',
            'bar',
        ]
        self.cacher = cacher.WynnCacher()

    def test_true(self):
        """
        _any_in_any returns True when an item is found in a sequence
        """
        self.assertTrue(self.cacher._any_in_any(self.in_a_sequence, self.sequences))

    def test_false(self):
        """
        _any_in_any returns False when no item is found in any sequence
        """
        self.assertFalse(self.cacher._any_in_any(self.not_in_a_sequence, self.sequences))


class TestDictMinMax(TestCase):
    """Test the utility function _dict_min_max"""

    def setUp(self):
        self.limit = {
            'key': (5, 10)
        }
        self.limit_min = {
            'key': (5, None)
        }
        self.limit_max = {
            'key': (None, 10)
        }
        self.values_in_range = {
            'key': 7
        }
        self.values_below_range = {
            'key': 3
        }
        self.values_above_range = {
            'key': 12
        }
        self.values_no_key = {
            'key2': 7
        }
        self.cacher = cacher.WynnCacher()

    def test_in_range(self):
        """
        _dict_min_max with value in range returns True
        """
        self.assertTrue(self.cacher._dict_min_max(self.limit, self.values_in_range))

    def test_below_range(self):
        """
        _dict_min_max with value below range returns False
        """
        self.assertFalse(self.cacher._dict_min_max(self.limit, self.values_below_range))

    def test_above_range(self):
        """
        _dict_min_max with value above range returns False
        """
        self.assertFalse(self.cacher._dict_min_max(self.limit, self.values_above_range))

    def test_above_min(self):
        """
        _dict_min_max with value above minimum returns True
        """
        self.assertTrue(self.cacher._dict_min_max(self.limit_min, self.values_in_range))

    def test_below_min(self):
        """
        _dict_min_max with value below minimum returns False
        """
        self.assertFalse(self.cacher._dict_min_max(self.limit_min, self.values_below_range))

    def test_below_max(self):
        """
        _dict_min_max with value below maximum returns True
        """
        self.assertTrue(self.cacher._dict_min_max(self.limit_max, self.values_in_range))

    def test_above_max(self):
        """
        _dict_min_max with value above maximum returns False
        """
        self.assertFalse(self.cacher._dict_min_max(self.limit_max, self.values_above_range))

    def test_missing_key(self):
        """
        _dict_min_max with missing key returns False
        """
        self.assertFalse(self.cacher._dict_min_max(self.limit, self.values_no_key))


@patch('urllib.request.urlopen', mock_urllib.mock_urlopen)
class TestGetIngredient(TestCase):
    """Test the get_ingredient function

    The ingredient cache and HTTP responses are mocked.
    """

    def setUp(self):
        self.cacher = cacher.WynnCacher()
        self.cacher.cache['ingredient']['Existing Ingredient'] = ObjectFromDict({
            'name': 'Existing Ingredient',
        })

    def test_get_ingredient_with_existing_ingredient(self):
        """
        get_ingredient with existing ingredient returns the ingredient
        """
        self.assertIsNotNone(self.cacher.get_ingredient('Existing Ingredient'))

    def test_get_ingredient_with_uncached_ingredient(self):
        """
        get_ingredient with uncached ingredient fetches the ingredient
        """
        self.assertIsNotNone(self.cacher.get_ingredient('Valid Ingredient'))

    def test_get_ingredient_with_invalid_ingredient(self):
        """
        get_ingredient with invalid ingredient returns None
        """
        self.assertIsNone(self.cacher.get_ingredient('Invalid Ingredient'))


class TestSearchIngredients(TestCase):
    """Test the search_ingredients function

    The ingredient cache is mocked.
    """

    def setUp(self):
        self.cacher = cacher.WynnCacher()
        self.cacher.cache['ingredient']['Item A'] = ObjectFromDict({
            'name': 'Item A',
            'level': 7,
            'tier': 1,
            'skills': ['WOODWORKING'],
            'identifications': {
                'SPEED': {
                    'minimum': 5,
                    'maximum': 10,
                },
                'THORNS': {
                    'minimum': 5,
                    'maximum': 10,
                },
            },
            'itemOnlyIDs': {
                'durabilityModifier': 3,
                'strengthRequirement': 0,
                'dexterityRequirement': 0,
                'intelligenceRequirement': 0,
                'defenceRequirement': 5,
                "agilityRequirement": 0,
            },
        })
        self.cacher.cache['ingredient']['Item B'] = ObjectFromDict({
            'name': 'Item B',
            'level': 12,
            'tier': 3,
            'skills': ['ARMOURING'],
            'identifications': {
                'SPEED': {
                    'minimum': 15,
                    'maximum': 20,
                },
                'POISON': {
                    'minimum': 5,
                    'maximum': 10,
                },
            },
            'itemOnlyIDs': {
                'durabilityModifier': 8,
                'strengthRequirement': 5,
                'dexterityRequirement': 0,
                'intelligenceRequirement': 0,
                'defenceRequirement': 0,
                "agilityRequirement": 0,
            },
        })

    def test_level_filter(self):
        """
        Ingredients get filtered by level
        """
        result = self.cacher.search_ingredients(level_max=10)
        self.assertEqual(len(result), 1)
        self.assertIs(result[0], self.cacher.cache['ingredient']['Item A'])
        result = self.cacher.search_ingredients(level_min=10)
        self.assertEqual(len(result), 1)
        self.assertIs(result[0], self.cacher.cache['ingredient']['Item B'])

    def test_tier_filter(self):
        """
        Ingredients get filtered by tier
        """
        result = self.cacher.search_ingredients(tier_max=2)
        self.assertEqual(len(result), 1)
        self.assertIs(result[0], self.cacher.cache['ingredient']['Item A'])
        result = self.cacher.search_ingredients(tier_min=2)
        self.assertEqual(len(result), 1)
        self.assertIs(result[0], self.cacher.cache['ingredient']['Item B'])

    def test_skill_filter(self):
        """
        Ingredients get filtered by a single skill
        """
        result = self.cacher.search_ingredients(skills_include='WOODWORKING')
        self.assertEqual(len(result), 1)
        self.assertIs(result[0], self.cacher.cache['ingredient']['Item A'])
        result = self.cacher.search_ingredients(skills_include='ARMOURING')
        self.assertEqual(len(result), 1)
        self.assertIs(result[0], self.cacher.cache['ingredient']['Item B'])

    def test_skills_filter(self):
        """
        Ingredients get filtered by a list of skills
        """
        result = self.cacher.search_ingredients(skills_include=['WOODWORKING', 'ARMOURING'])
        self.assertEqual(len(result), 2)
        result = self.cacher.search_ingredients(skills_include=['WOODWORKING'])
        self.assertEqual(len(result), 1)
        self.assertIs(result[0], self.cacher.cache['ingredient']['Item A'])
        result = self.cacher.search_ingredients(skills_include=['WEAPONSMITHING'])
        self.assertEqual(len(result), 0)
        result = self.cacher.search_ingredients(skills_include=[])
        self.assertEqual(len(result), 0)

    def test_identifications_filter(self):
        """
        Ingredients get filtered by identifications
        """
        result = self.cacher.search_ingredients(identifications_include={'SPEED': (5, 10)})
        self.assertEqual(len(result), 1)
        self.assertIs(result[0], self.cacher.cache['ingredient']['Item A'])
        result = self.cacher.search_ingredients(identifications_include={'SPEED': (15, 20)})
        self.assertEqual(len(result), 1)
        self.assertIs(result[0], self.cacher.cache['ingredient']['Item B'])
        result = self.cacher.search_ingredients(identifications_include={'SPEED': (5, 20)})
        self.assertEqual(len(result), 2)
        result = self.cacher.search_ingredients(identifications_include={'THORNS': (None, None)})
        self.assertEqual(len(result), 1)
        self.assertIs(result[0], self.cacher.cache['ingredient']['Item A'])
        result = self.cacher.search_ingredients(identifications_include={'POISON': (None, None)})
        self.assertEqual(len(result), 1)
        self.assertIs(result[0], self.cacher.cache['ingredient']['Item B'])
        result = self.cacher.search_ingredients(identifications_include={})
        self.assertEqual(len(result), 2)
        result = self.cacher.search_ingredients(identifications_include={'LOOTBONUS': (None, None)})
        self.assertEqual(len(result), 0)

    def test_item_only_ids_filter(self):
        """
        Ingredients get filtered by itemOnlyIDs
        """
        result = self.cacher.search_ingredients(item_only_ids={'durabilityModifier': (0, 5)})
        self.assertEqual(len(result), 1)
        self.assertIs(result[0], self.cacher.cache['ingredient']['Item A'])
        result = self.cacher.search_ingredients(item_only_ids={'durabilityModifier': (5, 10)})
        self.assertEqual(len(result), 1)
        self.assertIs(result[0], self.cacher.cache['ingredient']['Item B'])
        result = self.cacher.search_ingredients(item_only_ids={'durabilityModifier': (1, 10)})
        self.assertEqual(len(result), 2)
        result = self.cacher.search_ingredients(item_only_ids={'defenceRequirement': (5, 10)})
        self.assertEqual(len(result), 1)
        self.assertIs(result[0], self.cacher.cache['ingredient']['Item A'])
        result = self.cacher.search_ingredients(item_only_ids={'strengthRequirement': (5, 10)})
        self.assertEqual(len(result), 1)
        self.assertIs(result[0], self.cacher.cache['ingredient']['Item B'])
        result = self.cacher.search_ingredients(item_only_ids={})
        self.assertEqual(len(result), 2)
        result = self.cacher.search_ingredients(item_only_ids={'dexterityRequirement': (1, None)})
        self.assertEqual(len(result), 0)
