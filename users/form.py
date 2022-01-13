from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField,  EmailField
from wtforms.validators import DataRequired, EqualTo, Length


class UserForm(FlaskForm):
    name = StringField('Имя', validators=[DataRequired()])
    username = StringField('Никнейм', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    color = StringField('Любимый цвет')
    password = PasswordField('Пароль', validators=[
                             DataRequired(), EqualTo('password2', message='пароли должны совпадать'), Length(min=8)])
    password2 = PasswordField('Потдвердить пароль',
                              validators=[DataRequired()])
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
