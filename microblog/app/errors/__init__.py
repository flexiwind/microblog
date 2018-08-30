# coding=utf-8

"""
File Name： __init__.py
Created on: 8/29/18 5:07 PM
Author: feng
Description : 
"""
from flask import Blueprint

bp = Blueprint('errors', __name__)

from app.errors import handlers
