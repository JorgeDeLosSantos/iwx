# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name="iwx",
    version='0.1.0',
    description='wxPython utilities and enhanced controls',
    author='Pedro Jorge De Los Santos',
    author_email='delossantosmfq@gmail.com',
    license = "MIT",
    keywords=["wxPython","GUI"],
    install_requires=["tinycss"],
    url='https://github.com/JorgeDeLosSantos/iwx',
    packages=['iwx'],
    classifiers=[
      "Development Status :: 2 - Pre-Alpha",
      "Intended Audience :: Education",
      "Intended Audience :: Developers",
      "License :: OSI Approved :: MIT License",
      "Operating System :: OS Independent",
      "Programming Language :: Python",
      "Programming Language :: Python :: 2.7",
      "Programming Language :: Python :: Implementation :: CPython",
      "Topic :: Desktop Environment",
      "Topic :: Utilities",
    ],
    package_data={'iwx':['img/*']}
)
