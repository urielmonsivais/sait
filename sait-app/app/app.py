from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signin')
def signin():
    return render_template('signin.html')

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

@app.route('/prueba')
def prueba():
    return render_template('prueba.html')

@app.route('/servicios')
def servicios():
    return render_template('servicios.html')