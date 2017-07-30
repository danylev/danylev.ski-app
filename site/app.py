from flask import Flask
from flask import render_template, request, send_from_directory
app = Flask(__name__)


@app.route("/")
def main_page():
    return render_template('index.html',)


@app.route("/js/<path:path>")
def send_js(path):
    return send_from_directory('js', path)


@app.route("/img/<path:path>")
def send_img(path):
    return send_from_directory('img', path)


@app.route("/css/<path:path>")
def send_css(path):
    return send_from_directory('css', path)


@app.route("/font/roboto/<path:path>")
def send_font(path):
    return send_from_directory('font', path)


@app.route("/sass/<path:path>")
def send_sass(path):
    return send_from_directory('sass', path)


@app.route("/fonts/<path:path>")
def send_fonts(path):
    return send_from_directory('fonts', path)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
