from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User

class RegistrationForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    password2 = PasswordField("Reperat Password", validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField("Register")

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError("Please enter a different username")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError("Please enter a different email")

# class Loginform(FlaskForm):
#     def __init__(self, formdata=_Auto, **kwargs):
#         super().__init__(formdata, kwargs)
#         self.remember_me = None
#
#     username = StringField("Username", validators=[DataRequired()])
#     email = StringField("Email", validators=[DataRequired(), Email()])
#     password = PasswordField("Password", validators=[DataRequired()])
#     submit = SubmitField("Register")