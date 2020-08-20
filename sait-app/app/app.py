from flask import Flask, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost' 
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'sait_db'
mysql = MySQL(app)


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
	cur = mysql.connection.cursor()
	cur.execute("INSERT INTO activos (id,nombre,direccion) VALUES (%s,%s,%s)", (None, 'Test Action', 'Test Address'))
	mysql.connection.commit()
	return render_template('prueba.html')

@app.route('/Dashboard')
def Dashboard():
	cur = mysql.connection.cursor()
	cur.execute("SELECT activos.nombre , periodo_pago.f_termino, periodo_pago.f_corte , periodo_pago.f_pago FROM (periodo_pago LEFT JOIN activos  ON periodo_pago.id = activos.id) ")
	actions = cur.fetchall()
	cur.close()	
	print(actions)
	return render_template('Dashboard.html', actions = actions)

@app.route('/servicios')
def servicios():
    return render_template('servicios.html')
