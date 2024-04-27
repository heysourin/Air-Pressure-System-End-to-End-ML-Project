from setuptools import find_packages, setup
from typing import List

setup(
    name='sensor',
    version='0.0.0.1',
    author="sourin",
    author_email="sourin07@gmail.com",
    packages=find_packages(),
    install_require=["pymongo"],
    
)


'''
find_packages: Finds packages from your directory. It tries to find it using __init__.py.

'''
