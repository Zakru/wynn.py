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
----------

.. module:: wynn.guild

.. autofunction:: getGuilds

.. autofunction:: getGuild

Ingredient
----------

.. module:: wynn.ingredient

.. autofunction:: getIngredientNames

.. autofunction:: getIngredient
