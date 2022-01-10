from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class UserForm(FlaskForm):
    name = StringField('Как тебя зовут', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    color = StringField('Любимый цвет')
    submit = SubmitField('Отправить')
