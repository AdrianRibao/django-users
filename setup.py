#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import subprocess
from setuptools import setup, find_packages


version = '0.1.0'


if sys.argv[-1] == 'publish':
    subprocess.call(['python', 'setup.py', 'sdist', 'upload'])
    print "You probably want to also tag the version now:"
    print "  git tag -a %s -m 'Tag version %s'" % (version, version)
    print "  git push --tags"
    sys.exit()


setup(
    name='django-users',
    version=version,
    description='Django user registration with backends and tools',
    author='Adrián Ribao',
    url='http://gitlab.adrima.es/django-users/master/tree',
    packages=['django_users',],
    license='BSD',
)
