from setuptools import find_packages,setup
from typing import List



def get_requirments(file_path:str,) -> List[str]:
    '''
    this function will return a list of requirments
    '''
    reqirments = []
    with open(file_path) as file_obj:
        requirment = file_obj.readlines()
        requirment = [req.replace('\n','') for req in requirment]
        if '-e .' in requirment:
            requirment.remove('-e .')


setup (
    name = 'mlproject',
    version = '0.0.1',
    author = 'Saksham',
    author_email = 'sakshamkale46@gmail.com',
    packages = find_packages(),
    install_requires = ['pandas','numpy','seaborn','matplotlib'],
    install_requirments = get_requirments('requirments.txt')
)
