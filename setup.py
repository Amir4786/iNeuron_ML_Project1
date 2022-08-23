from setuptools import setup,find_packages
from typing import List

requirement_file_name="requirements.txt"
def get_requirements_list()->List[str]:
    """
    Description: This function gives the list of requirements
    from the file requirements.txt
    
    return: a list containing name of required libraries
    """
    with open(REQUIREMENTS_FILE_NAME) as requirement_file:
        return requirement_file.readline()

PROJECT_NAME="housing_predictor"
VERSION="0.0.3"
AUTHOR="AMIR KHAN"
DESCRIPTION="This is my first ever project"
PACKAGES=["housing"]
REQUIREMENTS_FILE_NAME="requirements.txt"

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