# coding=utf-8

"""
Setup script for pytvmaze
"""

from setuptools import setup
from pytvmaze.tvmaze import __version__

setup(
    name='pytvmaze',
    version='{0}.{1}.{2}'.format(*__version__),
    description='Python interface to the TV Maze API (www.tvmaze.com)',
    url='https://github.com/srob650/pytvmaze',
    author='Spencer Roberts',
    author_email='pytvmaze@gmail.com',
    license='MIT',

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5'
    ],

    keywords='python tv television tvmaze',
    packages=['pytvmaze'],
    requires=['requests'],
)
