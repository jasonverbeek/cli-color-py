#!/usr/bin/env python3.10 -mpoetry run python

from distutils.core import setup
import os

def read_file(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        return file.read()

setup(
    name='cli-color-py',
    version='0.2.0',
    description='Minimalistic way to add colors to your terminal output',
    long_description=read_file('README.md'),
    long_description_content_type='text/markdown',
    author='Jason Verbeek',
    author_email='jason@localhost8080.org',
    url='https://github.com/jasonverbeek/cli-color-py',
    download_url='https://github.com/jasonverbeek/cli-color-py/archive/refs/tags/0.2.0.tar.gz',
    packages=['cli_color'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ]
)
