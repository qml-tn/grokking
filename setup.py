
from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='tngrokking',
    version='0.0.1',
    description='Grokking phase transitions in learning local rules',
    long_description=readme,
    author='Bojan Žunkovič',
    author_email='bojan.zunkovic@fri.uni-lj.si',
    url='https://github.com/qml-tn/grokking.git',
    license=license,
    packages=["tngrokking"],
)
