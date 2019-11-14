"""
Gets the level of a user's class.
"""

import sys

from wynn.player import getPlayer

def getLevel():
    user = sys.argv[1]
    cls = sys.argv[2]

    print(getPlayer(user).classesDict[cls].level)

usage = """
Usage:
  python get_level.py <user> <class>

Gets the level of the specified class of the specified Wynncraft user.
"""

if sys.argv[1] == '--help':
    print(usage)
else:
    getLevel()
