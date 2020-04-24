# Code by:Faiaz Amin Khan


# please install flask_mail
# Command: pip install Flask-Mail
# Enable permission here: https://www.google.com/settings/security/lesssecureapps

from flask import Flask, request, url_for
from flask_mail import Message, Mail
from itsdangerous import URLSafeTimedSerializer, SignatureExpired

SECRET_SERIALIZER = URLSafeTimedSerializer('SHANAIERSHUR!')

# this function takes an email address and send a confirmation message to the client
# it generates the token itself
def send_mail(email):
    token = SECRET_SERIALIZER.dumps(email, salt='email-confirm')
    msg = Message('Confirm Email', sender='faiazamin443@gmail.com', recipients=[email])
    link = url_for('confirm_email', token=token, _external=True)
    msg.body = 'Your link is {}'.format(link)
    return msg