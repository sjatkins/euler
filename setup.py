__author__ = 'samantha'
from setuptools import setup, find_packages
packages = find_packages(exclude=['test'])

setup(name='euler',
      version='0.1',
      description='ai explorations',
      author='Samantha Atkins',
      author_email='sjatkins@protonmail.com',
      license='internal',
      packages=packages,
      install_requires = ['sjautils'],
      zip_safe=False)
