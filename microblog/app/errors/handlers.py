# coding=utf-8

"""
File Name： handlers
Created on: 8/29/18 5:07 PM
Author: feng
Description : 
"""
from flask import render_template
from app import db
from app.errors import bp


@bp.app_errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404


@bp.app_errorhandler(500)
def not_found_error(error):
    db.session.rollback()
    return render_template('errors/500.html'), 500