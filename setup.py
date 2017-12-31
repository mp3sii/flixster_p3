# /usr/bin/env python

try:
    from setuptools import setup
    from setuptools import find_packages
except ImportError:
    from distutils.core import setup

setup(
    name='Export Flixster Ratings Python 3',
    version='0.0.1',
    description='Flixster ratings Python API',
    keywords='flixster ratings movies',
    author='Angel Saiz',
    packages=[find_packages()],
    # python_requires='>3.2',
    install_requires=["requests"]

)
# TODO delete or fix setup.py
# TODO complete readme.md