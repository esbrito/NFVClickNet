#!/usr/bin/env python

"Setuptools params"

from setuptools import setup, find_packages
from os.path import join

# Get version number from source tree
import sys
sys.path.append( '.' )
from mininet.net import VERSION

scripts = [ join( 'bin', filename ) for filename in [ 'mn' ] ]

modname = distname = 'mininet'

setup(
    name=distname,
    version=VERSION.replace("d", ""),
    description='Process-based OpenFlow emulator',
    author='Bob Lantz',
    author_email='rlantz@cs.stanford.edu',
    packages=[ 'mininet', 'mininet.examples' ],
    long_description="""
        Mininet is a network emulator which uses lightweight
        virtualization to create virtual networks for rapid
        prototyping of Software-Defined Network (SDN) designs
        using OpenFlow. http://mininet.org
        """,
    classifiers=[
          "License :: OSI Approved :: BSD License",
          "Programming Language :: Python",
          "Development Status :: 5 - Production/Stable",
          "Intended Audience :: Developers",
          "Topic :: System :: Emulators",
    ],
    keywords='networking emulator protocol Internet OpenFlow SDN',
    license='BSD',
    install_requires=[
        'setuptools',
        'urllib3',
        'docker==2.0.2',
        'pytest',
        'docker-py>=1.7.1',
        'ryu>=4',
        'networkx>=1.10',
        'spyne==2.12.11',
        'suds>=0.4',
        'lxml>=2.3',
        'debtcollector>=1.2.0',
        'stevedore>=1.10.0',
        'greenlet>=0.3',
        'humanize'
    ],
    scripts=scripts,
)
