from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import StringField, SubmitField, PasswordField,  EmailField, TextAreaField
from wtforms.validators import DataRequired, EqualTo, Length


class UserForm(FlaskForm):
    name = StringField('Имя', validators=[DataRequired()])
    username = StringField('Никнейм', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired()])
    about_author = TextAreaField('О пользователе')
    password = PasswordField('Пароль', validators=[
                             DataRequired(), EqualTo('password2', message='пароли должны совпадать'), Length(min=8)])
    password2 = PasswordField('Потдвердить пароль',
                              validators=[DataRequired()])
    profile_pic = FileField('Иконка пользователя')
    submit = SubmitField('Отправить')


class NameForm(FlaskForm):
    name = StringField('Имя', validators=[DataRequired()])
    submit = SubmitField('Отправить')


class PasswordForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    submit = SubmitField('Войти')


class LogindForm(FlaskForm):
    username = StringField('Никнейм', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    submit = SubmitField('Войти')
