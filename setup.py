from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file: str) -> List[str]:
    '''Returns a list of requirements'''
    requirements = []
    with open(file, 'r') as f:
        requirements = f.readlines()
        requirements = [req.replace('\n', '') for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name="ML practise",
    version='0.0.1',
    author="Abhinav",
    author_email='abhi9v2204@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
