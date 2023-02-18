from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, TextAreaField
from wtforms.validators import InputRequired, Email

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired()])
    subject = StringField('Email', validators=[InputRequired()])
    email = StringField('Subject', validators=[InputRequired(), Email()])
    message = TextAreaField('Message', validators=[InputRequired()])