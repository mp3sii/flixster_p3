#!~/.virtualenvs/flixsterP3/bin/python3.5

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='Export Flixster Ratings Python 3',
    version='0.0.1',
    description='Flixster ratings Python API',
    keywords='flixster ratings movies',
    author='Angel Saiz',
    packages=['ratings'],
    install_requires=['requests']

)
