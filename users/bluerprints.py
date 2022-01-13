from flask import Blueprint, render_template, flash, request
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from flask.helpers import url_for
from werkzeug.utils import redirect
import bcrypt

from db import db
from .models import Users
from .form import LogindForm, UserForm, NameForm, PasswordForm

user = Blueprint('user', __name__, template_folder='templates')

login_manager = LoginManager()
login_manager.login_view = 'user.login'
login_manager.login_message = 'Авторизуйтесь для доступа к закрытым страницам'


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


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
        if Users.query.filter_by(name=form.name.data).first() is None:
            if Users.query.filter_by(username=form.username.data).first() is None:
                if Users.query.filter_by(email=form.email.data).first() is None:
                    password = form.password.data.encode('utf-8')
                    hash = bcrypt.hashpw(password, bcrypt.gensalt())
                    user = Users(name=form.name.data, username=form.username.data,
                                 email=form.email.data, color=form.color.data, password=hash.decode('utf8'))
                    db.session.add(user)
                    db.session.commit()
                    flash('Пользователь добавлен')
                else:
                    flash('Регистрация не удалась!Такой email уже заренистрирован!')
                    return render_template('user/add.html', form=form)
            else:
                flash('Регистрация не удалась!Такой никнейм уже заренистрирован!')
                return render_template('user/add.html', form=form)
        else:
            flash('Регистрация не удалась!Такое имя уже зарегестрировано!')
            return render_template('user/add.html', form=form)
        name = form.name.data
        form.name.data = ''
        form.username.data = ''
        form.email.data = ''
        form.color.data = ''
        form.password.data = ''
    our_users = Users.query.order_by(Users.created_add)
    return render_template('user/add.html', name=name, form=form, our_users=our_users)


@user.route('/login', methods=['GET', 'POST'])
def login():
    form = LogindForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(username=form.username.data).first()
        if user:
            if bcrypt.checkpw(form.password.data.encode('utf-8'), user.password.encode('utf-8')):
                login_user(user)
                return redirect('/')
            else:
                flash('Неправильный пароль!')
        else:
            flash('Нет такого пользователя!')
    return render_template('user/login.html', form=form)


@user.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    form = UserForm()
    return render_template('user/dashboard.html', form=form)


@user.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    flash('Вы вышли из системы')
    return redirect(url_for('user.login'))


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
        form.email.data = ''
        form.password.data = ''
        user = Users.query.filter_by(email=email).first()
        passed = bcrypt.checkpw(password, user.password.encode('utf-8'))
    return render_template('user/test_pw.html', form=form, email=email, user=user, passed=passed, password=password)


@user.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    form = UserForm()
    name_to_update = Users.query.get_or_404(id)
    if request.method == 'POST':
        name_to_update.name = request.form['name']
        name_to_update.username = request.form['username']
        name_to_update.email = request.form['email']
        name_to_update.color = request.form['color']
        try:
            db.session.commit()
            flash('Данные обновленны')
            return redirect(url_for('user.dashboard'))
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
        return redirect(url_for('user.register'))
    except:
        flash('Ошибка! Попробуй еще раз...')
        return redirect(url_for('user.register'))
