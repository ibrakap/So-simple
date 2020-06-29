from setuptools import setup

setup(
    name='simple dirb',
    version='0.1',
    description='A simple dirb tool for simple operations',
    license='The Unlicence',
    author='ibrakap',
    url='https://github.com/ibrakap/simple_dirb',
    entry_points={
    'console_scripts': ['sdirb = dirb:main',],
    }
)