#!/usr/bin/env python

from distutils.core import setup

CLASSIFIERS = [
	'Development Status :: 1 - Beta',
	'Intended Audience :: Developers',
	'License :: OSI Approved :: Apache Software License',
	'Topic :: Networking :: Printer Discovery',
	'Topic :: Software Development :: Libraries'
]
long_desc = ''This is a tool to locate and create a list of printers on a given network.
It has dependencies with nmap and net-snmp-devel along with easysnmp and python-nmap'''

setup(name='python-printer-locator',
	version='0.0.1',
	description='Python library for locating printers on a given network',
	long_description=long_desc,
	author='Lucas Brictson',
	author_email='ljbrictson@gmail.com',
	maintainer='Lucas Brictson',
	maintainer_email='ljbrictson@gmail.com',
	url='https://github.com/lbrictson/python-printer-locator',
	packages=['python-printer-locator'],
	install_requires=['easysnmp', 'python-nmap'],
	license='Apache 2.0',
	classifiers=CLASSIFIERS
	)
