"""
The build/compilations setup

>> pip install -r requirements.txt
"""

from setuptools import setup

setup(
    name='simple-coin-detection',
    version='1.0',
    description='Simple coin detection and counting using OpenCV',
    author='Gustavo Paschoal',
    author_email='gpmiranda93@gmail.com',
    url='https://github.com/gustavopaschoal/simple-coin-detection',
	packages=['coincounter']
)