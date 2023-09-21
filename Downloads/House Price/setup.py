from setuptools import find_packages, setup
from typing import List


Hyphen_Dot = "-e ."
def get_requirements(file_path:str) -> List[str]:
    requirements = []

    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements if req != Hyphen_Dot]
    
    return requirements

setup(
    name="Regression Problem",
    version= "0.0.1",
    author="Oshionwu Victor",
    author_email= "omolevictor97@gmail.com",
    install_requires= get_requirements("requirements.txt"),
    packages= find_packages()
)