from os.path import exists
from setuptools import setup

setup(name='itertoolz',
      version='0.4',
      description='More iterator tools',
      url='http://github.com/mrocklin/itertoolz',
      author='Matthew Rocklin',
      author_email='mrocklin@gmail.com',
      license='BSD',
      packages=['itertoolz'],
      long_description=open('README.md').read() if exists("README.md") else "",
      zip_safe=False)
