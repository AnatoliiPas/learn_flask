from flask import Blueprint, render_template, flash, request
from flask.helpers import url_for
from werkzeug.utils import redirect
import bcrypt

from db import db
from .models import Users
from .form import UserForm, NameForm, PasswordForm

user = Blueprint('user', __name__, template_folder='templates')


@user.route('/name', methods=['GET', 'POST'])
def users():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        flash('Форма заполнена')
    return render_template('user/user.html', name=name, form=form)


@user.route('/register', methods=['GET', 'POST'])
def register():
    name = None
    form = UserForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        if user is None:
            password = form.password.data.encode('utf-8')
            hash = bcrypt.hashpw(password, bcrypt.gensalt())
            user = Users(name=form.name.data,
                         email=form.email.data, color=form.color.data, password=hash.decode('utf8'))
            db.session.add(user)
            db.session.commit()
        name = form.name.data
        form.name.data = ''
        form.email.data = ''
        form.color.data = ''
        form.password.data = ''
        flash('Пользователь добавлен')
    our_users = Users.query.order_by(Users.created_add)
    return render_template('user/add.html', name=name, form=form, our_users=our_users)


@user.route('/test_pw', methods=['GET', 'POST'])
def test_pw():
    email = None
    password = None
    user = None
    passed = None
    form = PasswordForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data.encode('utf-8')
        print(password)
        form.email.data = ''
        form.password.data = ''
        user = Users.query.filter_by(email=email).first()
        print(type(user.password))
        passed = bcrypt.checkpw(password, user.password.encode('utf-8'))
    return render_template('user/test_pw.html', form=form, email=email, user=user, passed=passed, password=password)


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
        return redirect(url_for('user.register'))
