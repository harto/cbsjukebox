from os.path import dirname, join
from setuptools import setup, find_packages

setup(
    name='cbsjukebox',
    install_requires=[
        'beautifulsoup4',
        'gdata',
        'sh',
        'youtube_dl',
    ],

    packages=find_packages(),

    entry_points={
        'console_scripts': [
            'cbsjukebox=cbsjukebox:main',
        ],
    },
)
