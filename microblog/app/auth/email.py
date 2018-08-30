# coding=utf-8

"""
File Name： email
Created on: 8/29/18 5:33 PM
Author: feng
Description : 
"""
from flask import current_app, render_template
from app.email import send_email


def send_password_reset_email(user):
    token = user.get_reset_password_token()
    print(token)
    send_email(
        '[Microblog] Reset Your Password',
        sender=current_app.config['ADMINS'][0],
        recipients=[user.email],
        text_body=render_template('email/reset_password.txt', user=user, token=token),
        html_body=render_template('email/reset_password.html', user=user, token=token)
    )
    print('email has sended!')