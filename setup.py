from setuptools import setup, find_packages

setup(
    name = 'opener',
    version = '0',
    packages = find_packages(),
    author = 'Cory Schwartz',
    entry_points = {
      'console_scripts': [
        'opener = opener.cli:main'
      ]
    }
)
