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

.. autofunction:: getPlayer

.. autoclass:: Player
   :members:

Guild
-----

.. module:: wynn.guild

.. autofunction:: getGuilds

.. autofunction:: getGuild

.. autoclass:: Guild
   :members:

Ingredient
----------

.. module:: wynn.ingredient

.. autofunction:: getIngredientNames

.. autofunction:: getIngredient

.. autofunction:: searchIngredients

Recipe
------

.. module:: wynn.recipe

.. autofunction:: getRecipeIDs

.. autofunction:: getRecipe

.. autofunction:: searchRecipes

Network
-------

.. module:: wynn.network

.. autofunction:: getServers

.. autofunction:: getPlayerSum

Leaderboard
-----------

.. module:: wynn.leaderboard

.. autofunction:: getGuildLeaderboard

.. autofunction:: getPlayerLeaderboard

.. autofunction:: getPVPLeaderboard

Territory
---------

.. module:: wynn.territory

.. autofunction:: getTerritories

Search
------

.. module:: wynn.search

.. autofunction:: search

Item
----

.. module:: wynn.item

.. autofunction:: searchItem
