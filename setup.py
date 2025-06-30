from setuptools import find_packages, setup

setup(
    name='compiler',
    version='2.0',
    packages=find_packages(include=['AFD', 'main','scanner','Token','DTO','TokenMapper', 'SymbolTable', 'Error', 'Parser', 'Semantic'])
)