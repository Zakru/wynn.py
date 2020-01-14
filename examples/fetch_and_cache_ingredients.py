"""
Fetches and caches ingredients from the Wynncraft API. Subsequent
executions read from the cache instead of re-fetching the ingredients.
Note that this program will create a file in the execution directory.
"""

import os

from wynn.ext.cacher import WynnCacher

cacher = WynnCacher(autosave='wynn_ingredients.cache')

if os.path.isfile('wynn_ingredients.cache'):
    with open('wynn_ingredients.cache', 'rb') as f:
        cacher.load_cache(f)

if len(cacher.cache['ingredient']) == 0:
    # Cache is empty, let's fetch the data.
    cacher.fetch_ingredients()

# Print "Rotten Flesh" directly from the cache
print(cacher.cache['ingredient']['Rotten_Flesh'])

# Cache gets automatically saved.
