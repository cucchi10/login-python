from flask import Flask, redirect, render_template, request, url_for, flash
from flask_mysqldb import MySQL
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager, login_manager, login_user, logout_user, login_required

from config import config

# Models
from models.ModelUser import ModelUser

# Entities
from models.entities.User import User

app=Flask(__name__)

csrf = CSRFProtect()
db= MySQL(app)
login_manager_app = LoginManager(app)

@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_by_id(db, id)


@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # print(request.form['username'])
        # print(request.form['password'])
        user = User(0,request.form['username'],request.form['password'])
        logged_user=ModelUser.login(db,user)
        if logged_user != None:
            if logged_user.password:
                login_user(logged_user)
                return redirect(url_for('home'))
            else:
                flash("Invalid password...")
                return render_template('auth/login.html')
        else:
            flash("User Not Found...")
            return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')


@app.route('/logout')
def logout():
    logout_user()
    return render_template('auth/login.html')

@app.route('/home')
@login_required # solo logeado puedo acceder al url, dejamos solo 1 el resto libre para test
def home():
    return render_template('home.html')

# error 401 y 404 con redireccion
def status_401(error):
    return redirect(url_for('login'))

def status_404(error):
    return redirect(url_for('home'))

# paginas test a hueviar 

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/paginatest1')
def paginatest1():
    return render_template('paginatest1.html')

@app.route('/paginatest2')
def paginatest2():
    return render_template('paginatest2.html')

@app.route('/paginatest3')
def paginatest3():
    return render_template('paginatest3.html')

@app.route('/paginatest4')
def paginatest4():
    return render_template('paginatest4.html')

@app.route('/paginatest5')
def paginatest5():
    return render_template('paginatest5.html')

if __name__ == '__main__':
    app.config.from_object(config['developement'])
    csrf.init_app(app) # proteccion csrf
    app.register_error_handler(401, status_401)
    app.register_error_handler(404, status_404)
    app.run()