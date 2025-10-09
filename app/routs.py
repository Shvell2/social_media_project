from flask import Flask, redirect, render_template, url_for, flash
from app.models import User
from app.forms.registrform import RegistrationForm
from app import db
from flask_login import current_user
from app import create_app

app = create_app
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