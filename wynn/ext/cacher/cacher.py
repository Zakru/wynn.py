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

import pickle
import sys

from ... import ingredient
from ...requests import ObjectFromDict


class WynnCacher:
    """Utility class for caching frequent requests to the Wynncraft API

    :param file: An optional file to initialize the cache from
    :type file: :term:`file object`
    :param autosave: An optional file path for automatic saving of the
       cache when this instance gets deleted
    :type autosave: :class:`str`
    """

    def __init__(self, file=None, autosave=None):
        if file is None:
            self.cache = {
                'ingredient': {},
            }
        else:
            self.load_cache(file)

        self.autosave = autosave

    def load_cache(self, file):
        """Load a previously saved cache file

        :param file: The file to load cached data from
        :type file: :term:`binary file`
        """
        self.cache = pickle.load(file)
        self._add_key_if_not_present('ingredient')

    def save_cache(self, file):
        """Save the cache to a file for future use

        :param file: The file to save the cached data to
        :type file: :term:`binary file`
        """
        pickle.dump(self.cache, file)

    def _add_key_if_not_present(self, key):
        if key not in self.cache:
            self.cache[key] = {}

    def get_ingredient(self, name):
        """Get a single ingredient object. If it is not cached, fetch
        it and cache it, otherwise return it from the cache.

        :param name: The name of the ingredient to get
        :type name: :class:`ObjectFromDict
           <wynn.requests.ObjectFromDict>`
        """
        if name not in self.cache['ingredient']:
            self.cache['ingredient'][name] = ingredient.get_ingredient(name)
        return self.cache['ingredient'][name]

    def fetch_ingredients(self):
        """Fetch information for every ingredient from Wynncraft and
        cache it. This method always replaces the current contents of
        the ingredient cache.

        .. note::

           For now, uses a request to
           ``/ingredient/search/skills/^woodworking,weaponsmithing,armouring,tailoring,cooking,alchemism,scribing,jeweling``,
           as it seems to be the only way to get the required data in a
           single request.
        """
        for i in ingredient.search_ingredients(
                'skills',
                '^woodworking,weaponsmithing,armouring,tailoring,cooking,alchemism,scribing,jeweling',
                ):
            self.cache['ingredient'][i.name] = i

    def search_ingredients(self, *, name_includes=None, level_min=None,
            level_max=None, tier_min=None, tier_max=None, skills_include=None,
            identifications_include=None, durability_min=None,
            durability_max=None, item_only_ids=None):
        """Search the cached ingredients. All keyword arguments may be
        combined. Leaving one as ``None`` disables it.
        :meth:`fetch_ingredients` should be called first to fetch the
        information for all ingredients if it has not been loaded from a
        cache.

        It is recommended to use this method instead of
        :func:`wynn.ingredient.search_ingredients` to avoid making
        excessive requests to the HTTP API.

        :param name_includes: Filter names by keywords
           (case-insensitive)
        :type name_includes: :class:`str`
        :param level_min: Filter with a minimum level (inclusive)
        :type level_min: :class:`int`
        :param level_max: Filter with a maximum level (inclusive)
        :type level_max: :class:`int`
        :param tier_min: Filter with a minimum tier (inclusive)
        :type tier_min: :class:`int`
        :param tier_max: Filter with a maximum tier (inclusive)
        :type tier_max: :class:`int`
        :param skills_include: Filter ingredients only usable in a
           specific skill or one skill. Match ingredients whose
           ``skills`` contains a string which contains either this
           argument (if this argument is a :class:`str`) or any item
           in this argument (assumed to be an iterable).
        :type skills_include: :class:`str` or :term:`iterable`
        :param identifications_include: Filter identifications. Should
           be a :class:`dict` of :class:`tuple` objects where the key
           is the identification name and the tuple contains a min and
           max value respectively (set either to ``None`` to disable
           that limit)
        :type identifications_include: :class:`dict`
        :param item_only_ids: Filter itemOnlyIDs. Should
           be a :class:`dict` of :class:`tuple` objects where the key
           is the itemOnlyID name and the tuple contains a min and max
           value respectively (set either to ``None`` to disable that
           limit)
        :type item_only_ids: :class:`dict`

        :returns: The ingredients that matched the query
        :rtype: :class:`list`
        """
        ingredients = self.cache['ingredient'].values()
        if name_includes is not None:
            ingredients = filter(lambda i: self._all_in(name_includes.lower().split(' '), i.name.lower()), ingredients)
        if level_min is not None:
            ingredients = filter(lambda i: i.level >= level_min, ingredients)
        if level_max is not None:
            ingredients = filter(lambda i: i.level <= level_max, ingredients)
        if tier_min is not None:
            ingredients = filter(lambda i: i.tier >= tier_min, ingredients)
        if tier_max is not None:
            ingredients = filter(lambda i: i.tier <= tier_max, ingredients)
        if skills_include is not None:
            if isinstance(skills_include, str):
                ingredients = filter(lambda i: self._in_any(skills_include, i.skills), ingredients)
            else:
                ingredients = filter(lambda i: self._any_in_any(skills_include, i.skills), ingredients)
        if identifications_include is not None:
            ingredients = filter(lambda i: self._identifications(identifications_include, i.identifications), ingredients)
        if item_only_ids is not None:
            ingredients = filter(lambda i: self._dict_min_max(item_only_ids, i.itemOnlyIDs), ingredients)

        return list(ingredients)

    def __del__(self):
        # Autosave
        if self.autosave is not None:
            with open(self.autosave, 'wb') as f:
                self.save_cache(f)

    def _in_any(self, item, sequences):
        """Return ``True`` if ``item`` is found in any of the
        sequences in ``sequences``

        :param item: The item to find
        :param sequences: The sequences to check

        :returns: ``True`` if the item is found in any of the
            sequences, ``False`` otherwise
        :rtype: :class:`bool`
        """
        for s in sequences:
            if item in s:
                return True
        return False

    def _all_in(self, items, sequence):
        """Return ``True`` if all of ``items`` are found in ``sequence``

        :param item: The items to find
        :param sequences: The sequence to check

        :returns: ``True`` if the item is found in any of the
            sequences, ``False`` otherwise
        :rtype: :class:`bool`
        """
        for item in items:
            if item not in sequence:
                return False
        return True

    def _any_in_any(self, iterable_in, sequences):
        """Return ``True`` if any of the items in ``iterable_in``
        are found in any of the sequences in ``sequences``

        :param iterable_in: An iterable of the items to find
        :type iterable_in: :term:`iterable`

        :returns: ``True`` if any of the items are found in any of
            the sequences, ``False`` otherwise
        :rtype: :class:`bool`
        """
        for item in iterable_in:
            if self._in_any(item, sequences):
                return True
        return False

    def _dict_min_max(self, dict_limit, dict_values):
        """Return ``True`` if all the values in ``dict_values`` are
        inside the corresponding bounds found in ``dict_limit``

        Example::

            >>> dict_limit = { 'key': (5, 10) }
            >>> cacher._dict_min_max(dict_limit, { 'key': 7 })
            True
            >>> cacher._dict_min_max(dict_limit, { 'key': 4 })
            False

        :param dict_limit: A dict of 2-tuples whose elements are a
            minimum and maximum value respectively (both inclusive).
            Set one to ``None`` to disable it.
        :type dict_limit: :class:`dict`
        :param dict_values: A dict of values to be checked against
            ``dict_limit``. If a key is missing, ``False`` is
            returned.
        :type dict_values: :class:`dict`

        :returns: ``True`` if all the values in ``dict_values``
            match the limits in ``dict_limit``, ``False`` otherwise
        :rtype: :class:`bool`
        """
        for k,v in dict_limit.items():
            if k not in dict_values:
                return False
            if v[0] is not None:
                if v[0] > dict_values[k]:
                    return False
            if v[1] is not None:
                if v[1] < dict_values[k]:
                    return False

        return True

    def _identifications(self, identifications_include, identifications):
        for k,v in identifications_include.items():
            if k not in identifications:
                return False
            if v[0] is not None:
                if v[0] > identifications[k]['minimum']:
                    return False
            if v[1] is not None:
                if v[1] < identifications[k]['maximum']:
                    return False

        return True
