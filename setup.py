from setuptools import setup,find_packages
from typing import List

requirement_file_name="requirements.txt"
def get_requirements_list():
    """
    Description: This function gives the list of requirements
    from the file requirements.txt
    
    return: a list containing name of required libraries
    """
    with open(requirement_file_name) as requirement_file:
        return requirement_file.readline().remove("-e .")

PROJECT_NAME="housing_predictor"
VERSION="0.0.1"
AUTHOR="AMIR KHAN"
DESCRIPTION="This is my first ever project"
PACKAGES=["housing"]

setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=get_requirements_list()
    
    )

"""
python setup.py install
"""