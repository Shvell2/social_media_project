from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from basic_flask_project import app
from app.models import User

from flask import Flask,redirect,render_template,url_for, flash
from app.models import User
from app.forms.registrform import RegistrationForm
from flask_login import login_user, logout_user, current_user

app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

@app.route("/")
def main_page():

    return render_template("index.html")

@app.route("/registr_page")
def registration():
    if current_user.is_authenticated:
        return redirect(url_for('templates.index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('auth.login'))
    return render_template('register.html', title='Register', form=form)
