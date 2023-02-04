#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='shared',
      version='1.2.3',
      description='This package has shared components.',
      author='Efrain Olivares, Joshua Choi',
      author_email='efrain.olivares@gmail.com',
      packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
      license='LICENSE.txt',
    )
