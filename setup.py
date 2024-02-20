from setuptools import setup, find_packages

setup(
    name='myPackage',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA example of python package',
    long_description=open( 'README.md').read(),
    install_requires= ['numpy'],
    url='https://github.com/mbarndouka/packagePy',
    author='Mbarndouka',
    author_email='mmbarndouka@gmail.com',
)