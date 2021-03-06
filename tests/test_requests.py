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

    def test_get_dict_value(self):
        """
        Can get a simple value from an ObjectFromDict using dict style
        access
        """
        obj = ObjectFromDict(self.dict)
        self.assertEqual(obj['string'], 'value')

    def test_get_dict_value_from_dict(self):
        """
        Can get a value from a dict in an ObjectFromDict using dict
        style access
        """
        obj = ObjectFromDict(self.dict)
        self.assertEqual(obj['dict']['string2'], 'value2')

    def test_get_dict_value_from_list(self):
        """
        Can get a value from a list in an ObjectFromDict using dict
        style access
        """
        obj = ObjectFromDict(self.dict)
        self.assertEqual(obj['list'][0], 'value3')

    def test_get_dict_value_from_dict_in_list(self):
        """
        Can get a value from a dict in a list in an ObjectFromDict using
        dict style access
        """
        obj = ObjectFromDict(self.dict)
        self.assertEqual(obj['list'][1]['string4'], 'value4')
