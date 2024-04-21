from setuptools import find_packages, setup


setup(name='melhousing', 
    version='1.0', 
    packages=find_packages(include=['AFD', 'main','scanner', 'symbol_table']))