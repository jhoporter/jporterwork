from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, validators
from wtforms.validators import DataRequired, ValidationError, Email

class ContactForm(FlaskForm):
    name = StringField('Name')
    email = StringField('Email', validators=[DataRequired(), Email()])
    article_type = StringField('Article Type')
    word_count = StringField('Word Count')
    message = TextAreaField('Message')
    submit = SubmitField('Submit')
