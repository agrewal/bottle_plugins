#!/usr/bin/env python

import sys
import os
from distutils.core import setup

try:
    from distutils.command.build_py import build_py_2to3 as build_py
except ImportError:
    from distutils.command.build_py import build_py

setup(
    name = 'bottle-renderer',
    version = '0.1.1',
    url = 'https://github.com/agreatjewel/bottle_plugins/tree/master/bottle_renderer',
    description = 'Renderer plugin for bottle',
    long_description = open('README.rst').read(),
    author = 'Ajeet Grewal',
    author_email = 'asgrewal@gmail.com',
    license = 'MIT',
    platforms = 'any',
    py_modules = [
        'bottle_renderer'
    ],
    requires = [
        'bottle (>=0.9)'
    ],
    classifiers = [
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    cmdclass = {'build_py': build_py}
)

