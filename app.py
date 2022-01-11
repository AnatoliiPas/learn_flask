from os import name
from flask import Flask, render_template
from flask_migrate import Migrate

from db import db

from config import Config
from users.bluerprints import user
from differents.bluerprints import different


app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
maigrate = Migrate(app, db)


app.register_blueprint(user, url_prefix='/user')
app.register_blueprint(different, url_prefix='/different')


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
