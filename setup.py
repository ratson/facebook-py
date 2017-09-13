#!/usr/bin/env python
from setuptools import setup

with open('facebook/version.py') as f:
    exec(f.read())

with open('README.rst') as f:
    long_description = f.read()

setup(
    name='facebook-py',
    version=__version__,
    description='This client library is designed to support the Facebook '
                'Graph API and the official Facebook JavaScript SDK, which '
                'is the canonical way to implement Facebook authentication.',
    author='Ratson',
    url='https://github.com/ratson/facebook-py',
    license='Apache',
    packages=["facebook"],
    long_description=long_description,
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5'
    ],
    install_requires=[
        'requests',
    ],
)
