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

from .requests import requestPlain, ObjectFromDict

def getGuilds():
    """Gets a list of guild names from the Wynncraft API. Uses
    https://docs.wynncraft.com/Guild-API/#list.

    :returns: A :class:`list` of :class:`str` containing the names of
       all Wynncraft guilds.
    :rtype: :class:`list`
    """
    return requestPlain(
        'https://api.wynncraft.com/public_api.php?action=guildList'
        )['guilds']

def getGuild(name):
    """Gets a guild's information from the Wynncraft API. Uses
    https://docs.wynncraft.com/Guild-API/#statistics.

    :param name:
    :type name: :class:`str`

    :returns: The information of the guild as returned by the API
    :rtype: :class:`ObjectFromDict <wynn.requests.ObjectFromDict>`
    """
    return Guild(requestPlain(
        'https://api.wynncraft.com/public_api.php?action=guildStats&command={0}',
        name
        ))

class Guild(ObjectFromDict):
    """Contains Guild data in the Wynncraft API format. The format may
    be found at https://docs.wynncraft.com/Guild-API/#statistics.

    :param data: The parsed JSON data from the Wynncraft API
    :type data: :class:`dict`

    :ivar owner: The owner member of this guild
    :vartype owner: :class:`str`
    """

    def __init__(self, data):
        super(Guild, self).__init__(data)
        self.owner = [member for member in self.members if member.rank == 'OWNER'][0]
