# from flask_wtf import FlaskForm
# from wtforms import StringField, PasswordField, EmailField, SubmitField, BooleanField
# from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
# # from models import User
#
#
# class RegistrationForm(FlaskForm):
#     username = StringField('Имя пользователя',
#                            validators=[
#                                DataRequired(message='Обязательное поле'),
#                                Length(min=3, max=20, message='Имя пользователя должно быть от 3 до 20 символов')
#                            ],
#                            render_kw={"placeholder": "Введите имя пользователя", "class": "form-control"})
#
#     email = EmailField('Email',
#                        validators=[
#                            DataRequired(message='Обязательное поле'),
#                            Email(message='Введите корректный email адрес')
#                        ],
#                        render_kw={"placeholder": "Введите ваш email", "class": "form-control"})
#
#     password = PasswordField('Пароль',
#                              validators=[
#                                  DataRequired(message='Обязательное поле'),
#                                  Length(min=6, message='Пароль должен быть не менее 6 символов')
#                              ],
#                              render_kw={"placeholder": "Введите пароль", "class": "form-control"})
#
#     confirm_password = PasswordField('Подтвердите пароль',
#                                      validators=[
#                                          DataRequired(message='Обязательное поле'),
#                                          EqualTo('password', message='Пароли должны совпадать')
#                                      ],
#                                      render_kw={"placeholder": "Повторите пароль", "class": "form-control"})
#
#     agree_to_terms = BooleanField('Я согласен с условиями использования',
#                                   validators=[DataRequired(message='Необходимо принять условия использования')])
#
#     submit = SubmitField('Зарегистрироваться',
#                          render_kw={"class": "btn btn-primary btn-block"})
#
#     def validate_username(self, username):
#         user = User.query.filter_by(username=username.data).first()
#         if user:
#             raise ValidationError('Это имя пользователя уже занято. Выберите другое.')
#
#     def validate_email(self, email):
#         user = User.query.filter_by(email=email.data).first()
#         if user:
#             raise ValidationError('Этот email уже зарегистрирован.')