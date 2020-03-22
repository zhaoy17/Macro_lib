#!/usr/bin/env python

from setuptools import setup

with open("README.md") as f:
    long_description = f.read()

setup(
    name = 'macro_lib',
    version = '1.0',
    description = 'Python library providing computational tools for various macroeconomics models',
    license = "Apache License 2.0",
    long_description = long_description,
    author = 'Yixin (Peter) Zhao',
    author_email = 'peterzhao204@gmail.com',
    packages = ['macro_lib', 'macro_lib.solow'],
    url = 'https://github.com/zhaoy17/macro_lib',
    install_requires = [
        'pandas',
        'numpy',
    ],
    classifiers = [
        "Development Status :: 1 - Planning",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.0",
        "Topic :: Scientific/Engineering :: Computational Economics",
    ],
)

