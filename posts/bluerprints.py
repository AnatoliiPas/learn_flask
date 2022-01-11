from flask import Blueprint, render_template, flash

from db import db
from .models import Posts
from .form import PostForm

post = Blueprint('post', __name__, template_folder='templates')


@post.route('/add-post', methods=['GET', 'POST'])
def add_post():
    form = PostForm()

    if form.validate_on_submit():
        post = Posts(title=form.title.data, content=form.content.data,
                     autor=form.autor.data, slug=form.slug.data)
        form.title.data = ''
        form.content.data = ''
        form.autor.data = ''
        form.slug.data = ''

        db.session.add(post)
        db.session.commit()
        flash('Ваш пост создан.')

    return render_template('posts/add_post.html', form=form)
