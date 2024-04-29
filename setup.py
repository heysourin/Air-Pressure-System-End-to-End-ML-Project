from typing import List
from setuptools import find_packages, setup


def get_requirements() -> List[str]:
    requirements_list: List[str] = [] #returns list of requirements
    return requirements_list


setup(
    name='sensor',
    version='0.0.0.1',
    author="sourin",
    author_email="sourin07@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(), 
    )

'''
find_packages: Finds packages from your directory. It tries to find it using __init__.py.

'''
