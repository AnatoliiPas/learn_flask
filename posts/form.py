from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.widgets import TextArea
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    title = StringField('Название', validators=[DataRequired()])
    content = StringField('Контент', validators=[
        DataRequired()], widget=TextArea())
    autor = StringField('Автор', validators=[DataRequired()])
    slug = StringField('Slug', validators=[DataRequired()])
    submit = SubmitField('Отправить')
