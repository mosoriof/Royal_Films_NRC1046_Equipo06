from flask import render_template, redirect, request, url_for, flash, session
from markupsafe import escape
from werkzeug.security import check_password_hash, generate_password_hash
from app import db
from app.models import User, Movie
from .forms import LoginForm, SignupForm
from . import home

SALT = 'BnM02I$#R7'


@home.route('/', methods=["GET"])
def index():
    billboard = Movie.query.filter_by(status = 'active').all()
    releases = Movie.query.filter_by(status = 'new').all()
    return render_template('index.html', movies=billboard, news=releases)


@home.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        usuario = escape(request.form['user'])
        clave = escape(request.form['password'])
        
        user = User.query.filter_by(email=usuario).first()

        if user is not None:
            clave = SALT + clave + usuario
            user_id = user.user_id
            sw = check_password_hash(user.password, clave)
            if(sw):
                session['usuario'] = user.user_id
                session['nombre'] = user.name
                session['correo'] = user.email
                session['rol'] = user.role
                flash("Ha ingresado exitosamente")
                return redirect(url_for('user.perfil'))

        flash("Usuario/contraseña incorrecta", "errorLogin")
    return render_template('login.html', form=form)


@home.route('/register', methods=["GET", "POST"])
def register():
    form = SignupForm()
    if request.method == 'POST' and form.validate_on_submit():
        usuario = escape(request.form['userID'])
        nombre = escape(request.form['userName'])
        apellido = escape(request.form['userLastName'])
        correo = escape(request.form['userEmail'])
        telefono = escape(request.form['userPhone'])
        passw = escape(request.form['userPassword'])
        passwConf = escape(request.form['userPasswordConfirm'])

        # Buena práctica: generación de hash para contraseña. Se genera a partir del usuario(correo), la contraseña y SALT.
        passw = SALT + passw + correo
        passw = generate_password_hash(passw)
        
        user = User(user_id=usuario, name=nombre, lastname=apellido, email=correo, celNum=telefono, password=passw, role='user', status='active')
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('home.login'))
    else:
        return render_template('register.html', form=form)


@home.route('/cartelera')
def cartelera():
    billboard = Movie.query.filter_by(status = 'active').all()
    return render_template('cartelera.html', movies=billboard)


@home.route('/pelicula/<int:id>')
def pelicula(id):
    movie = Movie.query.filter_by(movie_id=id).first()
    return render_template('pelicula.html', movie=movie)

@home.route('/proximos')
def proximos():
    releases = Movie.query.filter_by(status = 'new').all()
    return render_template('proximos.html', movies=releases)    

@home.route('/buscar')
def buscar():
    return render_template('buscar.html')

@home.route('/confiteria')
def confiteria():
    return render_template('confiteria.html')


@home.route('/nosotros')
def nosotros():
    return render_template('nosotros.html')