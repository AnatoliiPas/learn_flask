from flask import Blueprint, render_template, flash, request, redirect
from flask.helpers import url_for

from db import db
from .models import Posts
from .form import PostForm

post = Blueprint('post', __name__, template_folder='templates')


@post.route('/')
def index():
    posts = Posts.query.order_by(Posts.date_posted)
    return render_template('posts/posts.html', posts=posts)


@post.route('/<int:id>')
def posts(id):
    post = Posts.query.get_or_404(id)
    return render_template('posts/posts.html', post=post)


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


@post.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_post(id):
    form = PostForm()
    post = Posts.query.get_or_404(id)
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        post.autor = form.autor.data
        post.slug = form.slug.data

        db.session.add(post)
        db.session.commit()
        flash('Данные обновленны.')
        return redirect(url_for('post.posts', id=post.id))
    form.title.data = post.title
    form.content.data = post.content
    form.autor.data = post.autor
    form.slug.data = post.slug
    return render_template('posts/edit.html', form=form, post=post)


@post.route('/delete/<int:id>')
def delete_post(id):
    to_delete = Posts.query.get_or_404(id)

    try:
        db.session.delete(to_delete)
        db.session.commit()
        flash('Статья удаленна')
    except:
        flash('Ошибка при удалении! Попробуй еще раз...')

    return redirect(url_for('post.index'))