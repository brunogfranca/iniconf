# -*- coding: utf-8 -*-
from ez_setup import use_setuptools
use_setuptools()
from setuptools import setup, find_packages


setup(
    name='iniconf',
    version='0.1.0',
    description='INI Config Creating/Parsing Tool',
    long_description=open('README.md').read(),
    url='https://github.com/brunogfranca/iniconf',
    author='Bruno Franca',
    author_email='bgfranca@gmail.com',
    license='LICENSE.txt',
    packages=find_packages()
)
