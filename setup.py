# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name = "pyremark",
    version = "0.1.0",
    author = "greatghoul",
    author_email = "greatghoul+pyremark@gmail.com",
    description = ("Remark slides utilities"),
    install_requires = ['clik', 'pyinotify'],
    platforms='any',
    license = "MIT",
    url = "http://www.g2w.me/tag/pyremark/",
    # packages=['remark'],
    scripts = ['remark.py']
)
