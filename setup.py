from setuptools import find_packages,setup
from typing import List 


HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
        This Function will return the list of requirements.
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements


setup(
    Name="ML Project",
    version="0.0.1",
    author="Sachin",
    author_email="m.sachinkr.2005@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)