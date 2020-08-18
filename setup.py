from setuptools import setup

setup(
   name='L1_per',
   version='0.1.0',
   author='Jack Lubin',
   author_email='jlubin@uci.edu',
   license='LICENSE.txt',
   description='Making the L1 code as written by Nathan Hara pip install-able',
   long_description=open('README.txt').read(),
   install_requires=[
       "pytest",
   ],
)
