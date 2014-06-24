#!/usr/bin/env python

from setuptools import setup, find_packages

dependencies = [
    # packages for which we want the latest stable version
    "pep8>=1.5.6",
    "pylint>=1.2.1",
    "nose>=1.3.2",
    # packages to freeze by default
    "cssmin==0.2.0",
    "pyscss==1.2.0",
    "gunicorn==0.17.2",
    "flask==0.10.1",
    "sqlalchemy==0.9.3",
    "psycopg2==2.5.2",
    "alembic==0.6.3",
    "flask-assets==0.8",
    "flask-bcrypt==0.6.0",
    "flask-script==2.0.5",
    "flask-login==0.2.11",
    "flask-wtf==0.9.5",
    "flask-debugtoolbar==0.9.0",
]

setup(
    name="Mongoose",
    version="0.1",
    url="https://github.com/nezaj/mongoose",
    packages=find_packages(),
    zip_safe=False,
    install_requires=dependencies
)
