#!/usr/bin/env python3

from setuptools import setup

import ledfx.consts as const

PROJECT_PACKAGE_NAME = "ledfx"
PROJECT_VERSION = const.PROJECT_VERSION
PROJECT_LICENSE = "The MIT License"
PROJECT_AUTHOR = "Austin Hodges"
PROJECT_AUTHOR_EMAIL = "austin.b.hodges@gmail.com"
PROJECT_MAINTAINER = "LedFx Developers"
PROJECT_MAINTAINER_EMAIL = "ledfx.app@gmail.com"
PROJECT_URL = "https://github.com/LedFx/LedFx"
PROJECT_WEBSITE = "https://ledfx.app"
PROJECT_DOCS = "https://ledfx.readthedocs.io"

# Need to install numpy first
SETUP_REQUIRES = [
    "numpy>=1.20.2",
    "wheel>=0.36.2",
]

INSTALL_REQUIRES = [
    "numpy>=1.20.2",
    "voluptuous>=0.12.0",
    "pyaudio>=0.2.11",
    "sacn==1.5.0",
    "aiohttp~=3.7.4.post0",
    "multidict>=5.0.0",
    "aiohttp_jinja2>=1.4.0",
    "requests>=2.24.0",
    "pyyaml>=5.3.1",
    "aubio>=0.4.9",
    # Zeroconf Bug introduced in 0.29
    # https://github.com/jstasiak/python-zeroconf/issues/337
    "zeroconf<=0.28.8||>=0.30.0",
    'pywin32>=300; platform_system == "Windows"',
    "cython>=0.29.21",
    "pyupdater>=4.0.0",
    "sentry-sdk~=1.1.0",
    "certifi>=2020.12.5",
    "pyserial>=3.5",
    "python-rtmidi>=1.4.9",
]

setup(
    name=PROJECT_PACKAGE_NAME,
    version=PROJECT_VERSION,
    license=PROJECT_LICENSE,
    author=PROJECT_AUTHOR,
    author_email=PROJECT_AUTHOR_EMAIL,
    maintainer=PROJECT_MAINTAINER,
    maintainer_email=PROJECT_MAINTAINER_EMAIL,
    url=PROJECT_URL,
    project_urls={
        "Documentation": PROJECT_DOCS,
        "Website": PROJECT_WEBSITE,
        "Source": PROJECT_URL,
        "Discord": "https://discord.gg/PqXMuthSNx",
    },
    install_requires=INSTALL_REQUIRES,
    setup_requires=SETUP_REQUIRES,
    python_requires=const.REQUIRED_PYTHON_STRING,
    entry_points={"console_scripts": ["ledfx = ledfx.__main__:main"]},
)
