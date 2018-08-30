# coding=utf-8

"""
File Name： __init__.py
Created on: 8/29/18 5:16 PM
Author: feng
Description : 
"""
from flask import Blueprint

bp = Blueprint('auth', __name__)

from app.auth import routes