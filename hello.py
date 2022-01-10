from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user/<name>')
def name(name: str):
    ctx = {'name': name}
    return render_template('user.html', ctx=ctx)


@app.errorhandler(404)
def erorr_page(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def erorr_page(e):
    return render_template('500.html'), 500
