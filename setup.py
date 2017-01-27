#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup
 
setup(
    name='facebook-py',
    version='0.1',
    description='This client library is designed to support the Facebook Graph API and the official Facebook JavaScript SDK, which is the canonical way to implement Facebook authentication.',
    author='Ratson',
    url='https://github.com/ratson/facebook-py',
    package_dir={'': 'src'},
    py_modules=[
        'facebook',
    ],
)
