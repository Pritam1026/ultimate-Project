from setuptools import setup,find_packages
from typing import List

PROJECT_NAME="Machine learning project"
VERSION="0.0.1"
DESCRIPTION="My new Ml project"
AUTHOR="Pritam"
AUTHOR_EMAIL="singhpritam983@gmail.com"

HYPHEN_E_DOT="-e ."

def get_requiremnets(file_path)->List[str]:
    with open(file_path,"r") as file_obj:
        requirement_list=file_obj.readlines()
        requirement_list=[req.replace("\n","") for req in requirement_list]

        if HYPHEN_E_DOT in requirement_list:
            requirement_list.remove(HYPHEN_E_DOT)

        return requirement_list

setup(
   name=PROJECT_NAME,
   version=VERSION,
   description=DESCRIPTION,
   author=AUTHOR,
   author_email=AUTHOR_EMAIL,
   packages=find_packages(),
   install_requires=get_requiremnets("requirements.txt")
)