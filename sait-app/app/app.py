from flask import (Flask, render_template, request,
                   g, session, url_for, redirect)
from flask_mail import Mail
from flask_mail import Message
from app.config.DB import DB
from app.auth.auth import Auth
from dotenv import load_dotenv
from app.users.Users import Users
from app.users.Providers import Providers
from app.users.Services import Services
from app.users.Software import Softwares
from app.users.Activos import Activos
#from app.users.Activos import activos
import os
load_dotenv()

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'monsivaisuriel28@gmail.com'
app.config['MAIL_PASSWORD'] = 'hpqgwjliswijqrwb'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.secret_key = os.getenv('SECRET_KEY')

cDb = DB()
mail = Mail(app)
auth = Auth(session, g, cDb)
skip_routes = ['signin','index','login','contact','static']




@app.route('/')
def index():
    return render_template('index.html')

@app.after_request
def after_request_func(response):    
    return response

@app.before_request
def before_request():    
    g.user = None    
    if 'current_user' in session:
        g.user = session['current_user']
    if auth.check_session() is None and request.endpoint not in skip_routes and request.endpoint:        
        return redirect(url_for('index'))
    
@app.route('/contact', methods=['POST'])
def contact():
    request_c = request.form
    try:
        msg = Message("Nueva Solicitud",
                      sender="monsivaisuriel28@gmail.com",
                      recipients=["uriel.monsivais@sait.red","hcedillo@sait.red"])
        mailBody = """ 
        Hola, nuevo correo de {0}.

        Datos:

            Nombre: {1}
            Telefono: {2}
            Numéro de empleados: {3}
            Servicios de interes: {4} 
        
        """.format(request_c['mail'], request_c['name'], request_c['phone'], request_c['employees'], request_c['services'])
        msg.body = mailBody
        mail.send(msg)
    except ValueError:
        print("Email error")
        print(ValueError)
    return render_template('index.html')
# aqui termina el mail

@app.route('/logout', methods=['GET'])
def logout():
    auth.logout()
    #return redirect(url_for('index'))
    return render_template('index.html')

@app.route('/signin', methods=['GET'])
def signin():
    return render_template('signin.html')

@app.route('/signin', methods=['POST'])
def login():
    try:
        data = request.form
        if auth.check_user(data['email'], data['password']):
            return redirect(url_for('dashboard'))
    except Exception as e:
        pass
    return render_template('signin.html')


@app.route('/welcome')
def welcome():
    return render_template('welcome.html')


@app.route('/dashboard')
def dashboard():
    software = Softwares(cDb)
    pendings = software.get_notifications()
    print(pendings)
    return render_template('Dashboard.html', pendings=pendings,actions=[],currentUser=session['current_user'])


@app.route('/servicios')
def servicios():
    return render_template('servicios.html')

#Usuarios 
@app.route('/users')
def users():
    users = Users(cDb)
    return render_template('users/users.html',users=users.getAll(),currentUser=session['current_user'])

@app.route('/users', methods=['POST'])
def postuser():
    req = request.form
    users = Users(cDb)
    users.add(req)
    del users
    return redirect(url_for('users'))

@app.route('/uusers', methods=['POST'])
def updateuser():
    req = request.form
    users = Users(cDb)
    users.update(req)
    del users
    return redirect(url_for('users'))

@app.route('/dusers', methods=['POST'])
def removeuser():
    req = request.form
    users = Users(cDb)
    users.remove(req)
    del users
    return redirect(url_for('users'))

#Proveedores
@app.route('/providers')
def providers():
    providers = Providers(cDb)    
    return render_template('providers/providers.html', providers=providers.getAll(),currentUser=session['current_user'])

@app.route('/providers', methods=['POST'])
def postprovider():
    req = request.form
    print(req)
    providers = Providers(cDb)
    providers.add(req)
    del providers
    return redirect(url_for('providers'))

@app.route('/uproviders', methods=['POST'])
def updateprovider():
    req = request.form
    providers = Providers(cDb)
    providers.update(req)
    del providers
    return redirect(url_for('providers'))

@app.route('/dproviders', methods=['POST'])
def removeprovider():
    req = request.form
    providers = Providers(cDb)
    providers.remove(req)
    del providers
    return redirect(url_for('providers'))

# Software
@app.route('/softwares')
def softwares():
    print(cDb)
    softwares = Softwares(cDb)
    return render_template('software/software.html', softwares=softwares.getAll(), types=softwares.getTypes(), providers=softwares.getProviders(), currentUser=session['current_user'])

@app.route('/software', methods=['POST'])
def postsoftware():
    req = request.form    
    softwares = Softwares(cDb)
    softwares.add(req)
    del softwares
    return redirect(url_for('softwares'))

@app.route('/usoftware', methods=['POST'])
def updatesoftware():
    req = request.form
    softwares = Softwares(cDb)
    softwares.update(req)
    del softwares
    return redirect(url_for('softwares'))

@app.route('/dsoftware', methods=['POST'])
def removesoftware():
    req = request.form
    softwares = Softwares(cDb)
    softwares.remove(req)
    del softwares
    return redirect(url_for('softwares'))

#Services
@app.route('/services')
def services():
    s = Services(cDb)
    return render_template('services/services.html',providers=s.getProviders(),services=s.getAll(),currentUser=session['current_user'])

@app.route('/services', methods=['POST'])
def postservice():
    req = request.form
    s = Services(cDb)
    s.add(req)
    del s
    return redirect(url_for('services'))

@app.route('/uservices', methods=['POST'])
def updateservice():
    req = request.form
    s = Services(cDb)
    s.update(req)
    del s
    return redirect(url_for('services'))

@app.route('/dservices', methods=['POST'])
def removeservice():
    req = request.form
    s = Services(cDb)
    s.remove(req)
    del s
    return redirect(url_for('services'))

# activos
@app.route('/activos')
def activos():
    s = Services(cDb)
    ac = s.getActivos()
    print(ac)
    return render_template('activos/activos.html',providers=s.getProviders(), activos=ac,actions=[],currentUser=session['current_user'])

@app.route('/activos', methods=['POST'])
def postactivos():
    req = request.form
    print("---")
    print(req)
    s = Activos(cDb)
    s.add(req)
    del s
    return redirect(url_for('activos'))

@app.route('/uactivos', methods=['POST'])
def updateactivos():
    req = request.form
    s = Activos(cDb)
    s.update(req)
    del s
    return redirect(url_for('activos'))

@app.route('/dactive', methods=['POST'])
def removeactivos():
    req = request.form
    s = Activos(cDb)
    s.remove(req)
    del s
    return redirect(url_for('activos'))

@app.route('/panel')
def panel():
    users = Users(cDb)
    c = users.getCompany()
    print(c.nombre)
    return render_template('panel.html',company=c,currentUser=session['current_user'])

@app.route('/update_company', methods=['POST'])
def update_company():
    req= request.form
    s=Users(cDb)
    s.updateCompany(req)
    del s
    return redirect(url_for('panel'))