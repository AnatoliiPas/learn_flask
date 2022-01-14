from re import search
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class SearchForm(FlaskForm):
    searched = StringField('Поиск', validators=[DataRequired()])
    submit = SubmitField('Поиск')
