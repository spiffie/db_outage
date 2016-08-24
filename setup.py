# coding: utf-8
# setup.py

"""A setuptools based setup module for db_outage.

See:
https://packaging.python.org/en/latest/distributing.html
"""

from setuptools import setup, find_packages

from codecs import open

from os import path

import db_outage


here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='db_outage',
    version=db_outage.__version__,

    description='A sample Python project',
    long_description=long_description,

    url='https://github.com/spiffie/ut-vprd-db-outage',

    author='David Voegtle',
    author_email='dvoegtle@austin.utexas.edu',

    license='Non-commercial',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: Free for non-commercial use',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        # 'Programming Language :: Python :: 3',
        # 'Programming Language :: Python :: 3.3',
        # 'Programming Language :: Python :: 3.4',
        # 'Programming Language :: Python :: 3.5',
    ],

    keywords='django database outage middleware',

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    install_requires=[
        'cx_Oracle',
        'django>=1.7,<2',
    ],

    # $ pip install -e .[dev,test]
    extras_require={
        # 'dev': ['check-manifest'],
        'test': ['coverage', 'mock'],
    },
)
