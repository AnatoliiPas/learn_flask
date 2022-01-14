from datetime import date
from flask import Blueprint, render_template

from .form import SearchForm
from posts.models import Posts


different = Blueprint('differents', __name__, template_folder='templates')


@different.route('/date-json')
def date_json():
    return {'date': date.today()}


@different.route('/search', methods=['POST'])
def search():
    form = SearchForm()
    posts = Posts.query
    if form.validate_on_submit():
        searched = form.searched.data
        posts = posts.filter(Posts.content.like('%' + searched + '%'))
        posts = posts.order_by(Posts.title).all()
        return render_template('differents/search.html', form=form, posts=posts)
