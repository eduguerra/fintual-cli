# -*- coding: utf-8 -*-


"""setup.py: setuptools control."""


import re
from setuptools import setup


version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('fintualcli/fintualcli.py').read(),
    re.M
    ).group(1)


with open("README.md", "rb") as f:
    long_descr = f.read().decode("utf-8")


setup(
    name = "cmdline-fintual-cli",
    packages = ["fintual-cli"],
    entry_points = {
        "console_scripts": ['fintual-cli = fintualcli.fintualcli:main']
        },
    version = version,
    description = "Unofficial CLI for Fintual API",
    long_description = long_descr,
    author = "Eduardo Guerra",
    author_email = "eeguerra@uc.cl",
    url = "",
    )
