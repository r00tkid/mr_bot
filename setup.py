# -*- coding: utf-8 -*-

#from distutils.core import setup
from setuptools import setup

setup(
  name='mr_bot',
  packages=['mr_bot'],
  version='1.1.0',
  description='Small package for assist telegram bot development',
  author='Root Kid',
  author_email='shaman@born2fish.ru',
  url='https://github.com/r00tkid/mr_bot.git',
  download_url='https://github.com/r00tkid/mr_bot/tarball/1.1.0',
  keywords=['support', 'telegram', 'bot', 'keyboard'],  # keywords
  classifiers=[],
  install_requires=[
      "emoji",
      'colored',
      'future',
      'mr-logger',
      'python-telegram-bot',
      'termcolor',
      'geopy',
      'urllib3'
  ],
)

