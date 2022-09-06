from setuptools import setup,find_packages
from typing import List
import housing


#Declaring variables for setup functions
PROJECT_NAME="housing_prediction"
VERSION="0.0.1"
AUTHOR="Ankur Shrivastava"
DESCRIPTION="This is first FSDS batch ML project"
REQUIREMENT_FILE_NAME="requirements.txt"

"""This function is going to retun list of requirments mention in requirements.txt files & this function is going to return list
   Which will contain name of libraries mentioned in requirements.txt files"""

def get_requirements_list()->List[str]:
    with open("REQUIREMENT_FILE_NAME") as requirement_file:
        return requirement_file.readlines().pop("-e .")


setup(
name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESCRIPTION,
packages=find_packages(),
install_requires=get_requirements_list()
)
 