#!/usr/bin/env/python

import os
from statictastic import metadata

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name = 'django-statictastic',
    version = metadata.__version__,
    license = metadata.__license__,
    description = 'A fantastic way to sync your files to S3.',
    long_description=long_description,
    author = metadata.__author__,
    author_email = metadata.__email__,
    packages=['statictastic'],
    install_requires=[],
)

