#!/usr/bin/env python3.10 -mpoetry run python

from distutils.core import setup

setup(
    name='cli-color-py',
    version='0.1.0',
    description='Minimalistic way to add colors to your terminal output',
    author='Jason Verbeek',
    author_email='jason@localhost8080.org',
    url='https://github.com/jasonverbeek/cli-color-py',
    download_url='https://github.com/jasonverbeek/cli-color-py/archive/refs/tags/0.1.0.tar.gz',
    packages=['cli_color'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ]
)
