# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name="iwx",
    version='0.1.0',
    description='wxPython custom controls',
    author='Pedro Jorge De Los Santos',
    author_email='delossantosmfq@gmail.com',
    license = "MIT",
    keywords=["wxPython","GUI"],
    install_requires=[""],
    url='https://github.com/JorgeDeLosSantos/iwx',
    packages=['iwx'],
    package_data={'iwx':['img/*']}
)
