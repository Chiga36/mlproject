## responsibe to create ML application as a package -> deploy in py py -> anybpdy can use it
from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    '''
    This function will return a list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        # removing the \n from each line
        requirements = [req.replace('\n','') for req in requirements]
        # removing the -e . from the requirements if present
        # -e . is used to install the package in editable mode whenever we run requirements.txt 
        # setup.txt should automatically run
        if '-e .' in requirements:
            requirements.remove('-e .')
    return requirements


setup(
    name='mlproject',
    version='0.0.1',
    author='Chirag',
    author_email='chigaswami@gmail.com',
    packages=find_packages(), # find all the packages in the directory
    install_requires=get_requirements('requirements.txt') # install all the requirements in the requirements.txt file
)
