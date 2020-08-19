#from setuptools import setup
try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

setup(
   name='L1_per',
   version='v0.3.0',
   author='Jack Lubin',
   author_email='jlubin@uci.edu',
   license='LICENSE.txt',
   description='Making the L1 code as written by Nathan Hara pip install-able',
   long_description=open('README.md').read(),
   #packages=setuptools.find_packages(),
   #packages=find_packages(), #fix
   install_requires=[
       "pytest",
   ],
)
