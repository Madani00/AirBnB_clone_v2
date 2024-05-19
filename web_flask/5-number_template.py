#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask, render_template


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def home():
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    return "HBNB"


@app.route('/c/<changeble_text>')
def c_is_c(changeble_text):
    text = changeble_text.replace("_", " ")
    return "C " + text


@app.route("/python/", defaults={'changeble_text': 'is cool'})
@app.route('/python/<changeble_text>')
def py(changeble_text):
    text = changeble_text.replace("_", " ")
    return "Python " + text


@app.route('/number_template/<int:n>')
def html_page(n):
    """display n if it's integer"""
    return render_template('5-number.html', name=n)


@app.route('/number/<int:n>')
def is_number(n):
    """display HTML page only if n it's integer"""
    return "{} is a number".format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
