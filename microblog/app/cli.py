# coding=utf-8

"""
File Name： cli
Created on: 8/28/18 5:46 PM
Author: feng
Description : 
"""
import subprocess

import os

from app import app


@app.cli.group()
def translate():
    """Translation and localization commands."""
    pass


@translate.command()
def update():
    """Update all languages."""
    if subprocess.run(['pybabel extract','-F babel.cfg', '-k', '_l', '-o messages.pot',' .']).returncode:
        raise RuntimeError('extract command failed')

    if subprocess.run(['pybabel update','-i messages.pot', '-d app/translations',]).returncode:
        raise RuntimeError('update command failed')

    os.remove('message.pot')


@translate.command()
def compile():
    """Compile all languages."""
    if subprocess.run(['pybabel compile', '-d app/translations']).returncode:
        raise RuntimeError('compile command failed')


