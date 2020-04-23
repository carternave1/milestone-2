from flask_wtf import FlaskForm  # Flask wrapper
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField

from wtforms.validators import DataRequired
class ReviewForm(FlaskForm):
    text = TextAreaField("Review", validators=[DataRequired()])
    submit = SubmitField('Sign In')
