from setuptools import find_packages,setup
from typing import List

hyphen_e_dot = '-e .'

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\nf","") for req in requirements]
        
        if hyphen_e_dot in requirements:
            requirements.remove(hyphen_e_dot)
            
    return requirements

setup(
    name='Regressor_Project',
    version='0.0.1',
    author='Fahad',
    author_email='ftkhan61814@gmail.com',
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages()
    )
