"""
The build/compilations setup

>> pip install -r requirements.txt
>> python setup.py install

"""

from setuptools import setup

setup(
    name='simple-coin-detection',
    version='1.0.0',
    description='Simple coin detection and counting using OpenCV',
    packages=['coincounter'],
    author='Gustavo Paschoal',
    author_email='gpmiranda93@gmail.com',
    url='https://github.com/gustavopaschoal/simple-coin-detection'	
)
