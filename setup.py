#!/usr/bin/env python

import os

from setuptools import setup

# if you are not using vagrant, just delete os.link directly,
# The hard link only saves a little disk space, so you should not care
if os.environ.get('USER','') == 'vagrant':
  del os.link


setup(
  name='harvey',
  version='0.0.1',
  description='harvey helps you manage and choose license from command line',
  long_description=open('README.rst').read(),
  author='Archit Verma',
  author_email='architv07@gmail.com',
  license='MIT',
  keywords=['license', 'legal', 'github', 'command line', 'cli'],
  url='https://github.com/architv/harvey',
  install_requires=[
    'docopt>=0.6.2',
    'requests==2.8.0',
    'colorama==0.3.3'
  ],
  entry_points={
    'console_scripts': [
      'harvey=harvey.harvey:main'
    ],
  }
)