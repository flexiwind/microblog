# coding=utf-8

"""
File Name： __init__.py
Created on: 8/29/18 5:41 PM
Author: feng
Description : 
"""
from flask import Blueprint

bp = Blueprint('main', __name__)

from app.main import routes