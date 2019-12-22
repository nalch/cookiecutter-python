"""
.. module:: setup
   :synopsis: Installation information for {{cookiecutter.package_name}}
"""
# Standard
import os
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

INSTALL_REQUIRES = ['setuptools']


setup(
    name='{{cookiecutter.package_name}}',
    version='{{cookiecutter.package_version}}',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    license='Apache-2.0',
    description='{{cookiecutter.project_description}}',
    long_description=README,
    long_description_content_type='text/x-rst',
    url='',
    author='',
    author_email='',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
    ],
    install_requires=INSTALL_REQUIRES,
)
