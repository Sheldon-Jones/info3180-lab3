from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Email, Length

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(message="Please enter your full name")])
    email = StringField('Email', validators=[DataRequired(message="Please enter your e-mail address"), Email(message="Please enter your e-mail address")])
    subject = StringField('Subject', validators=[DataRequired(message="Please enter an appropriate subject for your message")])
    message = TextAreaField('Message', validators=[DataRequired(message="Please enter the message you would like to send")])



