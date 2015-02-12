# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


setup(
    name='iniconf',
    version='0.1.9.1',
    description='INI Config Creating/Parsing Tool',
    long_description=open('README.md').read(),
    url='https://github.com/brunogfranca/iniconf',
    author='Bruno Franca',
    author_email='bgfranca@gmail.com',
    license=open('LICENSE.txt').read(),
    packages=find_packages(),
    entry_points={
        'console_scripts': ['iniconf = iniconf.cli:cli_main']
    }
)
