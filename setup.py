#!/usr/bin/env python

from distutils.core import setup

setup(name="glitch",
	version="1.0",
	description="glitch jpg files",
	author="trsqxyz",
	author_email="trsqxyz@gmail.com",
	url="https://github.com/trsqxyz",
	packages=["glitch",],
	entry_points={
		"console_scripts": [
			"glitch = glitch.glitch:main",
		]
	},
)
