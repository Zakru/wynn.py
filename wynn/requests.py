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

import json
import urllib

def requestList(url):
	"""Requests a list of objects from the Wynncraft API.
	
	:param url: The URL of the resource to fetch
	:type url: :class:`str`
	
	:returns: The returned JSON data in a :class:`dict`
	:rtype: :class:`dict`
	"""
	response = urllib.request.urlopen(urllib.parse.quote(url, ':/'))
	data = json.load(response)
	response.close()
	return data['data']

def request(url):
	"""Requests a single object from the Wynncraft API.
	
	:param url: The URL of the resource to fetch
	:type url: :class:`str`
	
	:returns: The returned JSON data in a :class:`dict`
	:rtype: :class:`dict`
	"""
	return requestList(url)[0]

class ObjectFromDict:
	"""Recursively wraps a :class:`dict` in a Python object.
	
	Example use::
	
	   >>> o = ObjectFromDict({'foo': 'bar'})
	   >>> o.foo
	   'bar'
	
	:param data: The parsed JSON data from the Wynncraft API
	:type data: :class:`dict`
	"""

	def __init__(self, data):
		for k,v in data.items():
			self.__dict__[k] = self.handleItem(v)

	def handleItem(self, item):
			if isinstance(item, dict):
				return ObjectFromDict(item)
			elif isinstance(item, list):
				return [self.handleItem(v) for v in item]
			else:
				return item
