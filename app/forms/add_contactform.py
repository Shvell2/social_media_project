from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User
from flask_wtf import FlaskForm

class Add_contactform(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])

