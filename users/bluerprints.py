from flask import Blueprint, render_template, flash, request
from flask.helpers import url_for
from werkzeug.utils import redirect
from werkzeug.security import generate_password_hash, check_password_hash

from db import db
from .models import Users
from .form import UserForm

user = Blueprint('user', __name__, template_folder='templates')


@user.route('/<name>')
def users(name: str):
    ctx = {'name': name}
    return render_template('user/user.html', ctx=ctx)


@user.route('/add', methods=['GET', 'POST'])
def add_user():
    name = None
    form = UserForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        if user is None:
            user = Users(name=form.name.data,
                         email=form.email.data, color=form.color.data)
            db.session.add(user)
            db.session.commit()
        name = form.name.data
        form.name.data = ''
        flash('Пользователь добавлен')
    our_users = Users.query.order_by(Users.created_add)
    return render_template('user/add.html', name=name, form=form, our_users=our_users)


@user.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    form = UserForm()
    name_to_update = Users.query.get_or_404(id)
    if request.method == 'POST':
        name_to_update.name = request.form['name']
        name_to_update.email = request.form['email']
        name_to_update.color = request.form['color']
        try:
            db.session.commit()
            flash('Данные обновленны')
            return redirect(url_for('user.add_user'))
        except:
            flash('Ошибка! Попробуй еще раз...')
            return render_template('user/update.html', form=form, name_to_update=name_to_update)
    return render_template('user/update.html', form=form, name_to_update=name_to_update, id=id)


@user.route('/delete/<int:id>')
def delete(id):
    user_to_delete = Users.query.get_or_404(id)
    try:
        db.session.delete(user_to_delete)
        db.session.commit()
        flash('Данные удалены')
        our_users = Users.query.order_by(Users.created_add)
        return redirect(url_for('user.add_user'))
    except:
        flash('Ошибка! Попробуй еще раз...')
        return redirect(url_for('user.add_user'))
