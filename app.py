from flask import Flask, render_template
from flask_migrate import Migrate

from conf import db, login_manager, ckeditor

from config import Config
from differents.form import SearchForm
from users.bluerprints import user
from differents.bluerprints import different
from posts.bluerprints import post


app = Flask(__name__)
app.config.from_object(Config)


db.init_app(app)
migrate = Migrate(app, db)
login_manager.init_app(app)
ckeditor.init_app(app)

app.register_blueprint(user, url_prefix='/user')
app.register_blueprint(post, url_prefix='/posts')
app.register_blueprint(different, url_prefix='/different')


@app.context_processor
def base():
    form = SearchForm()
    return dict(form=form)


@app.route('/')
def index():
    return render_template('index.html')


@app.errorhandler(404)
def erorr_page_n(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def erorr_page_s(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run()
