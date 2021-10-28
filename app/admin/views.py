from flask import render_template, redirect, request, url_for, flash, session
from markupsafe import escape
from app import db
from app.models import User, Movie
from werkzeug.security import check_password_hash, generate_password_hash
from .forms import LoginAdminForm, MovieForm
import functools

from . import admin

SALT = 'BnM02I$#R7'

def loginAdmin_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if 'isAdmin' not in session:
            return redirect(url_for('admin.admin_login'))
        return view(**kwargs)

    return wrapped_view

@admin.route('/', methods=["GET", "POST"])
def admin_login():
    form = LoginAdminForm()
    if request.method == 'POST' and form.validate_on_submit():
        usuario = escape(request.form['user'])
        clave = escape(request.form['password'])

        user = User.query.filter_by(email=usuario).first()

        if user is not None and user.role == 'admin':
            clave = SALT + clave + usuario
            user_id = user.user_id
            sw = check_password_hash(user.password, clave)
            if(sw):
                session['usuario'] = user.user_id
                session['nombre'] = user.name
                session['correo'] = user.email
                session['isAdmin'] = user.role
                flash("Ha ingresado exitosamente")
                return redirect(url_for('admin.admin_dashboard'))

        flash("No tiene acceso a esta página", "errorLoginA")
    return render_template('admin.html', form=form)


@admin.route('/dashboard/')
@loginAdmin_required
def admin_dashboard():
    return render_template('admin_dashboard.html')


@admin.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('admin.admin_login'))

@admin.route('/movies/', methods=["GET", "POST"])
@loginAdmin_required
def list_movies():
    movie = Movie.query.all()
    return render_template('list_movies.html', movie=movie)

@admin.route('/movies/add/', methods=["GET", "POST"])
@loginAdmin_required
def add_movie():
    form = MovieForm()
    if request.method == 'POST' and form.validate_on_submit():
        titulo = escape(request.form['movieTitle'])
        poster = escape(request.form['moviePoster'])
        trailer = escape(request.form['movieTrailer'])
        sinopsis = escape(request.form['movieSynopsis'])
        duracion = escape(request.form['movieLength'])
        formato = escape(request.form['movieFormat'])
        genero = escape(request.form['movieGenre'])
        clasif = escape(request.form['movieRating'])
        elenco = escape(request.form['movieCast'])
        estreno = escape(request.form['movieRelease'])
        
        movie = Movie(title=titulo, poster_file=poster, trailer_url=trailer,synopsis=sinopsis, length=duracion,format=formato, genre=genero, rating=clasif, cast=elenco, release=estreno, status='new')
        db.session.add(movie)
        db.session.commit()
        return redirect(url_for('admin.list_movies'))
    return render_template('add_movie.html', form=form)

@admin.route('/showtimes/', methods=["GET", "POST"])
@loginAdmin_required
def list_showtimes():
    return render_template('list_showtimes.html')

@admin.route('/showtimes/add/', methods=["GET", "POST"])
@loginAdmin_required
def add_showtimes():
    return render_template('add_showtimes.html')

@admin.route('/users/', methods=["GET", "POST"])
@loginAdmin_required
def list_users():
    return render_template('list_users.html')

@admin.route('/users-admin/', methods=["GET", "POST"])
@loginAdmin_required
def list_admins():
    return render_template('list_admins.html')

@admin.route('/bookings/', methods=["GET", "POST"])
@loginAdmin_required
def bookings():
    return render_template('bookings.html')

@admin.route('/admin2')
def admin2():
    return render_template('admin_dash2.html')
