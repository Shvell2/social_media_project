# @app.route("/")
# def main_page():
#
#     return render_template("index.html")
#
# @app.route("/registr_page")
# def registration():
#     if current_user.is_authenticated:
#         return redirect(url_for('templates.index'))
#     form = RegistrationForm()
#     if form.validate_on_submit():
#         user = User(username=form.username.data, email=form.email.data)
#         user.set_password(form.password.data)
#         db.session.add(user)
#         db.session.commit()
#         flash('Congratulations, you are now a registered user!')
#         return redirect(url_for('auth.login'))
#     return render_template('register.html', title='Register', form=form)