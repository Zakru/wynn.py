from setuptools import setup

with open('README.md', 'r') as f:
	readme = f.read()

setup(
	name='wynn.py',
	version='0.1.0a',
	author='Zakru',
	url='https://github.com/Zakru/wynn.py',
	description='A Python wrapper for the Wynncraft public API',
	long_description=readme,
	long_description_content_type='text/markdown',
	project_urls={
		'Documentation': 'https://wynnpy.readthedocs.io/en/latest/',
		'Source Code': 'https://github.com/Zakru/wynn.py',
		'Issue Tracker': 'https://github.com/Zakru/wynn.py/issues',
	},
	packages=['wynn'],
	classifiers=[
		'Development Status :: 3 - Alpha',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: MIT License',
		'Operating System :: OS Independent',
		'Programming Language :: Python :: 3',
		'Topic :: Games/Entertainment',
		'Topic :: Software Development :: Libraries',
	],
	)
