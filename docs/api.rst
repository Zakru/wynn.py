API Reference
=============

Requests
--------

.. module:: wynn.requests

The :mod:`wynn.requests` module contains internal utilities used by wynn.py.
Most importantly it contains the :class:`ObjectFromDict` class which is
used to convert :class:`dict`\s to objects.

.. autoclass:: ObjectFromDict
   :members:

Player
------

.. module:: wynn.player

.. autofunction:: get_player

.. autoclass:: Player
   :members:

Guild
-----

.. module:: wynn.guild

.. autofunction:: get_guilds

.. autofunction:: get_guild

.. autoclass:: Guild
   :members:

Ingredient
----------

.. module:: wynn.ingredient

.. autofunction:: get_ingredient_names

.. autofunction:: get_ingredient

.. autofunction:: search_ingredients

Recipe
------

.. module:: wynn.recipe

.. autofunction:: get_recipe_ids

.. autofunction:: get_recipe

.. autofunction:: search_recipes

Network
-------

.. module:: wynn.network

.. autofunction:: get_servers

.. autofunction:: get_player_sum

Leaderboard
-----------

.. module:: wynn.leaderboard

.. autofunction:: get_guild_leaderboard

.. autofunction:: get_player_leaderboard

.. autofunction:: get_pvp_leaderboard

Territory
---------

.. module:: wynn.territory

.. autofunction:: get_territories

Search
------

.. module:: wynn.search

.. autofunction:: search

Item
----

.. module:: wynn.item

.. autofunction:: search_item
