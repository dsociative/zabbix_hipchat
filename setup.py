#!/usr/bin/env python
# -*- coding: utf8 -*-

from setuptools import setup, find_packages


setup(
    name='zabbix_hipchat',
    author='dsociative',
    author_email='admin@geektech.ru',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'zabbix_hipchat = zabbix_hipchat.notify:main',
        ]
    },
    install_requires=[
        'sh'
    ]
)
