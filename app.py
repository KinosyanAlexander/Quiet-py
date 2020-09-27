from flask import Flask, send_file, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('2.html')


@app.route('/<path:path>')
def js(path):
    if path.startswith('javascripts'):
        return send_file(path)
