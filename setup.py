from setuptools import setup, find_packages

setup(
    name='simplediscord',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
        'websockets',
        'json',
        'asyncio',
        'functools',
    ],
)
