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

from .requests import requestLegacy, ObjectFromDict


def getServers():
    r"""Gets the currently active servers and the players on them.

    :returns: A :class:`dict` of :class:`list`\s by server name
       containing the names of the players connected to that server
    :rtype: :class:`dict`
    """
    return requestLegacy('https://api.wynncraft.com/public_api.php?action=onlinePlayers')


def getPlayerSum():
    """Gets the current number of players on the Wynncraft network.

    :returns: The number of players on the Wynncraft network
    :rtype: :class:`int`
    """
    return requestLegacy('https://api.wynncraft.com/public_api.php?action=onlinePlayersSum')['players_online']