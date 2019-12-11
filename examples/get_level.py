"""
Gets the level of a user's class.
"""

import sys

from wynn.player import get_player

def get_level():
    user = sys.argv[1]
    cls = sys.argv[2]

    print(get_player(user).classesDict[cls].level)

usage = """
Usage:
  python get_level.py <user> <class>

Gets the level of the specified class of the specified Wynncraft user.
"""

if len(sys.argv) == 1 or sys.argv[1] == '--help':
    print(usage)
else:
    get_level()
