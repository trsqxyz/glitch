#!/usr/bin/env python

from setuptools import setup


setup(
    name = "glitch",
    version = "1.3",
    description = "glitch jpg files",
    license = 'MIT',
    author = "trsqxyz",
    author_email = "trsqxyz@gmail.com",
    url = "https://github.com/trsqxyz/glitch",
    classifiers = [
        "Programming Language :: Python :: 3.4",
        "License :: OSI Approved :: MIT License"
    ],
    packages = ["glitch"],
    entry_points = """
        [console_scripts]
            glitch = glitch.glitch:main
        """,
    install_requires = [
        'docopt',
    ]
)
