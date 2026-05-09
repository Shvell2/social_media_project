from urllib.parse import urlsplit

from flask import Flask, redirect, render_template, url_for, flash, request, session
from app.models import User
from app.forms.registrform import RegistrationForm
from app.forms.loginform import Loginform
from flask_login import current_user, login_user, logout_user
from app import app, db
from flask_socketio import join_room, leave_room, send, SocketIO

socketio = SocketIO()
chats = {}
#настроить LoginManager

@app.route("/", methods=['GET', 'POST'])
def main_page():
    # if current_user.is_authenticated:
        # return redirect(url_for('index.html'))

    register_form = RegistrationForm(prefix="register")
    print(request.form)

    if "register-email" in request.form and register_form.validate_on_submit():
        user = User(username=register_form.username.data, email=register_form.email.data)
        user.set_password(register_form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        login_user(user, remember=True)
        return redirect(url_for('main_page'))

    login_form = Loginform(prefix="login")
    print(request.form)
    if "login-email" in request.form and login_form.validate_on_submit():
        user = db.session.scalar(db.select(User).where(User.username == login_form.username.data))
        if user is None or not user.check_password(login_form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('main_page'))
        login_user(user, remember=True)
        print("loget_in")
    flash(register_form.errors)
    flash(login_form.errors)
    return render_template('index.html', Register_form=register_form, Login_form=login_form, username=register_form.username.data)

@app.route("/add_friend/<username>", methods=['GET', 'POST'])
def add_friend(username):
    if username in db.session.query(User).all():
        user = User.query.filter_by(username = username).first()
        current_user.friends.append(user)
        db.session.commit()
    return redirect("main_page")



@socketio.on("message")
def message(data):
    chat = session.get("room")
    if chat not in chats:
        return
    content = {
        "name": session.get("name"),
        "message": data["data"]
    }
    send(content, to=chat)
    chats[chat]["messages"].append(content)
    print(f"{session.get('name')} said: {data['data']}")

# @app.route("/register", methods=["POST", "GET"])
# def register():
#     if current_user.is_authenticated:
#         return redirect(url_for('index.html'))
#     form = RegistrationForm()
#     if form.validate_on_submit():
#         user = User(username=form.username.data, email=form.email.data)
#         user.set_password(form.password.data)
#         db.session.add(user)
#         db.session.commit()
#         flash('Congratulations, you are now a registered user!')
#         return redirect(url_for('index.html'))
#     flash(form.errors)
#     return render_template('index.html', Register_form=form, username=form.username.data)

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     # if current_user.is_authenticated:
#     #     return redirect(url_for('main.index'))
#     form = Loginform()
#     if form.validate_on_submit():
#         user = db.session.scalar(db.select(User).where(User.username == form.username.data))
#         if user is None or not user.check_password(form.password.data):
#             flash('Invalid username or password')
#             return redirect(url_for('login.html'))
#         login_user(user, remember=form.remember_me.data)
#         # next_page = request.args.get('next')
#         # if not next_page or urlsplit(next_page).netloc != '':
#         #     next_page = url_for('index.html')
#         # return redirect(next_page)
#     return render_template('index.html', Login_form=form)

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    return redirect(url_for('main_page'))