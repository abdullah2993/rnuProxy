"""
Setup file for rnuProxy
"""
from setuptools import setup

setup(
    name='rnuProxy',
    version='0.1',
    scripts=['rnuProxy.py'],
    description='Download anime episodes from KissAnime',
    author='Abdullah Saleem',
    author_email='a.saleem2993@gmail.com',
    url='https://github.com/Abdullah2993/rnuProxy',
    license='MIT',
    keywords=['proxy', 'reverse proxy', 'ddns', 'noip', 'port forwarding'],
    install_requires=['tornado', 'maproxy', 'miniupnpc']
)