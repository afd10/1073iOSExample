try:
	from setuptools import setup
except: ImportError:
	from distutils.core import setup

config = {
		'description': 'My Project',
		'author': 'Jay Palat',
		'url': 'URL to get it at.',
		'dowload_url': 'Where to download it.',
		'author_email': 'jay@palat.net',
		'version': '0.1',
		'install_requires':['nose'],
		'packages': ['NAME'],
		'scripts': [],
		'name' : projectname'
}

setup (**config)
