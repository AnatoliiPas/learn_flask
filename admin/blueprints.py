from curses import flash
from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user

admin = Blueprint('admin', __name__, template_folder='templates')


@admin.route('/')
@login_required
def index():
    id = current_user.id
    if id == 31:
        return render_template('admin/admin.html')
    else:
        flash('Вы должны быть администратором.')
        return redirect(url_for('user.dashboard'))
