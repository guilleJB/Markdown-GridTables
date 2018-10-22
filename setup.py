#! /usr/bin/env python

from setuptools import setup

setup(
    name='mdx_grid_tables',
    version='1.2',
    author='smartboyathome',
    description='Python-Markdown extension to add grid_table support',
    url='https://github.com/smartboyathome/Markdown-GridTables/',
    py_modules=['mdx_grid_tables'],
    install_requires=['Markdown>=2.0',],
    entry_points={
        'markdown.extensions': [
            'grid_tables = mdx_grid_tables:GridTableExtension',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: BSD License',
        'Intended Audience :: Developers',
        'Environment :: Web Environment',
        'Programming Language :: Python',
        'Topic :: Text Processing :: Filters',
        'Topic :: Text Processing :: Markup :: HTML'
    ]
)
