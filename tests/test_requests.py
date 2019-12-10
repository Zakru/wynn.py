from unittest import TestCase

from wynn.requests import ObjectFromDict


class TestObjectFromDict(TestCase):
    """Test ObjectFromDict"""

    def setUp(self):
        self.dict = {
            'string': 'value',
            'dict': {
                'string2': 'value2',
            },
            'list': [
                'value3',
                {
                    'string4': 'value4',
                },
            ],
        }

    def test_get_value(self):
        """
        Can get a simple value from an ObjectFromDict
        """
        obj = ObjectFromDict(self.dict)
        self.assertEqual(obj.string, 'value')

    def test_get_value_from_dict(self):
        """
        Can get a value from a dict in an ObjectFromDict
        """
        obj = ObjectFromDict(self.dict)
        self.assertEqual(obj.dict.string2, 'value2')

    def test_get_value_from_list(self):
        """
        Can get a value from a list in an ObjectFromDict
        """
        obj = ObjectFromDict(self.dict)
        self.assertEqual(obj.list[0], 'value3')

    def test_get_value_from_dict_in_list(self):
        """
        Can get a value from a dict in a list in an ObjectFromDict
        """
        obj = ObjectFromDict(self.dict)
        self.assertEqual(obj.list[1].string4, 'value4')
