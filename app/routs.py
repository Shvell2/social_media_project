from urllib.parse import urlsplit

from flask import Flask, redirect, render_template, url_for, flash, request
from app.models import User
from app.forms.registrform import RegistrationForm, Loginform
from flask_login import current_user, login_user
from app import app, db



#настроить LoginManager

@app.route("/")
def main_page():

    return render_template('index.html')

@app.route("/registr_page", methods=["POST", "GET"])
def registration():
    if current_user.is_authenticated:
        return redirect(url_for('index.html'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('main_page'))
    return render_template('index.html', Register_form=form, username=form.username.data)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = Loginform()
    if form.validate_on_submit():
        user = db.session.scalar(
            db.select(User).where(User.username == form.username.data))
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login.html'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or urlsplit(next_page).netloc != '':
            next_page = url_for('main.index')
        return redirect(next_page)
    return render_template('index.html', Login_form=form)

