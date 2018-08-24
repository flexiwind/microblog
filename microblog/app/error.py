# coding=utf-8

"""
File Name： error
Created on: 8/22/18 3:18 PM
Author: feng
Description : 
"""
from flask import render_template

from app import app, db


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def not_found_error(error):
    db.session.rollback()
    return render_template('500.html'), 500
