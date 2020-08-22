from flask import Flask, render_template, request
from flask_mail import Mail
from flask_mail import Message
from app.config.DB import DB
#from flask_mysqldb import MySQL #<---los demas equipos
#from flaskext.mysql import MySQL #este es de kiike 

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost' 
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'farmacia'

mail = Mail(app)


@app.route('/')
def index():
    c = DB()
    return render_template('index.html')

# para el mail
@app.route('/contact', methods=['POST'])
def contact():
    request_c = request.form
    try:
        msg = Message("New request",
                  sender="monsivaisuriel28@gmail.com",
                  recipients=["uriel.monsivais@sait.red","enrique.espinoza@sait.red"])
        mailBody = """ 
        Hola, nuevo correo de {0}.

        Datos:

            Nombre: {1}
            Telefono: {2}
            Numéro de empleados: {3}
            Servicios de interes: {4} 
        
        """.format(request_c['mail'],request_c['name'],request_c['phone'],request_c['employees'],request_c['services'])
        msg.body = mailBody
        mail.send(msg)
    except ValueError:
        print("Email error")
        print(ValueError)
    return render_template('index.html')
#aqui termina el mail

@app.route('/signin')
def signin():
    return render_template('signin.html')

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

@app.route('/prueba')
def prueba():
	#cur = mysql.connection.cursor()
	#cur.execute("INSERT INTO activos (id,nombre,direccion) VALUES (%s,%s,%s)", (None, 'Test Action', 'Test Address'))
	#mysql.connection.commit()
	return render_template('prueba.html')

@app.route('/Dashboard')
def Dashboard():
	# cur = mysql.connection.cursor()
	# aqui empece
	# conn = mysql.connect()
	# cur=conn.cursor()
	# cur.execute("SELECT * FROM farmacia.acciones")
	# actions = cur.fetchall()
	# cur.close()	
	#print(actions)    
	return render_template('Dashboard.html', actions = [])

@app.route('/servicios')
def servicios():
    return render_template('servicios.html')
