# Code by:Faiaz Amin Khan


# please install flask_mail
# Command: pip install Flask-Mail
# Enable permission here: https://www.google.com/settings/security/lesssecureapps

from flask import Flask, request, url_for
from flask_mail import Message, Mail
from itsdangerous import URLSafeTimedSerializer, SignatureExpired

app = Flask(__name__)

# Checkout here
app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # if you want, you can use other mail server. But you need to configure
# it your self xD
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'YourMail'
app.config['MAIL_PASSWORD'] = 'Pass'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

s = URLSafeTimedSerializer('Thisisasecret!')


# this function takes an email address and send a confirmation message to the client
# it generates the token itself
def send_mail(email, link):
    @app.route('/', methods=['GET', 'POST'])
    def index():

        msg = Message('Confirm Email', sender='faiazamin443@gmail.com', recipients=[email])

        token = s.dumps("xlicjhhbgvtbftozxa@ttirv.org", salt='email-confirm')
        # link = url_for('confirm_email', token=token, _external=True)

        msg.body = 'Your link is {}'.format(link)

        mail.send(msg)

        return '<h1>The email you entered is {}. The token is {}</h1>'.format(email, token)

    @app.route('/confirm_email/<token>')
    def confirm_email(token):
        try:
            email = s.loads(token, salt='email-confirm', max_age=3600)
        except SignatureExpired:
            return '<h1>The token is expired!</h1>'
        return '<h1>The token works!</h1>'

    if __name__ == '__main__':
        app.run(debug=True)




send_mail('xlicjhhbgvtbftozxa@ttirv.org', "https://10minutemail.com/")
