from flask import render_template, redirect, request, url_for, flash, session
from markupsafe import escape
from app import db
from app.models import Booking, User, Movie, Screening
from werkzeug.security import check_password_hash, generate_password_hash
from .forms import LoginAdminForm, MovieForm, ShowtimeForm, AdminForm
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


def loginSuper_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if 'super' not in session:
            return redirect(url_for('admin.admin_dashboard'))
        return view(**kwargs)

    return wrapped_view


# Login Administrativo 
@admin.route('/', methods=["GET", "POST"])
def admin_login():
    form = LoginAdminForm()
    if request.method == 'POST' and form.validate_on_submit():
        usuario = escape(request.form['user'])
        clave = escape(request.form['password'])

        user = User.query.filter_by(email=usuario).first()

        if user is not None and (user.role == 'admin' or user.role == 'superadmin'):
            clave = SALT + clave + usuario
            user_id = user.user_id
            sw = check_password_hash(user.password, clave)
            if(sw):
                session['user'] = user.user_id
                session['name'] = user.name
                session['email'] = user.email
                session['isAdmin'] = user.role
                if user.role == 'superadmin':
                    session['super'] = True
                    session['name'] = user.name                   
                flash("Ha ingresado exitosamente")
                return redirect(url_for('admin.admin_dashboard'))

        flash("No tiene acceso a esta página", "errorLoginA")
    return render_template('admin.html', form=form)

# Dashboard administrativo
@admin.route('/dashboard/')
@loginAdmin_required
def admin_dashboard():
    mActive = Movie.query.filter_by(status = 'active').count()
    mNew = Movie.query.filter_by(status = 'new').count()
    fActive = Screening.query.filter_by(status = 'active').count()
    uActive = User.query.filter_by(status = 'active').count()
    
    cont = (mActive, mNew, fActive, uActive)
    return render_template('admin_dashboard.html', cont=cont)

# Cerrar sesión
@admin.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('admin.admin_login'))

# Listado de películas
@admin.route('/movies/', methods=["GET", "POST"])
@loginAdmin_required
def list_movies():
    movie = Movie.query.all()
    return render_template('list_movies.html', movie=movie)

# Agregrar Películas
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
        status = escape(request.form['movieStatus'])    
        movie = Movie(title=titulo, poster_file=poster, trailer_url=trailer,synopsis=sinopsis, length=duracion,format=formato, genre=genero, rating=clasif, cast=elenco, release=estreno, status=status)
        db.session.add(movie)
        db.session.commit()
        return redirect(url_for('admin.list_movies'))
    return render_template('add_movie.html', form=form)

# Eliminar Películas TO DO: agregar warning
@admin.route('/movies/del/<int:id>/', methods=["GET", "POST"])
@loginAdmin_required
def delete_movie(id):
    movie = Movie.query.filter_by(movie_id=id).first_or_404()
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('admin.list_movies'))

# Editar películas
@admin.route('/movies/edit/<int:id>', methods=["GET", "POST"])
@loginAdmin_required
def edit_movie(id=None):
    form = MovieForm()
    movie = Movie.query.get_or_404(id)
    if request.method == 'GET':
        form.movieTitle.data = movie.title
        form.moviePoster.data = movie.poster_file
        form.movieTrailer.data = movie.trailer_url
        form.movieSynopsis.data = movie.synopsis
        form.movieLength.data = movie.length
        form.movieFormat.data = movie.format
        form.movieGenre.data = movie.genre
        form.movieRating.data = movie.rating
        form.movieCast.data = movie.cast
        form.movieRelease.data = movie.release
        form.movieStatus.data = movie.status
    if form.validate_on_submit():
        data = form.data  
        movie.title = data['movieTitle']
        movie.poster_file = data['moviePoster'] 
        movie.trailer_url = data['movieTrailer'] 
        movie.synopsis = data['movieSynopsis'] 
        movie.length = data['movieLength'] 
        movie.format = data['movieFormat'] 
        movie.genre = data['movieGenre'] 
        movie.rating = data['movieRating'] 
        movie.cast = data['movieCast'] 
        movie.release = data['movieRelease'] 
        movie.status = data['movieStatus'] 
        db.session.add(movie)
        db.session.commit()
        return redirect(url_for('admin.list_movies'))
    return render_template('edit_movie.html', form=form, fun=id)


# Listado de Funciones
@admin.route('/showtimes/', methods=["GET", "POST"])
@loginAdmin_required
def list_showtimes():
    showTime = Screening.query.all()
    return render_template('list_showtimes.html', showTime=showTime)


# Agregar Funciones
@admin.route('/showtimes/add/', methods=["GET", "POST"])
@loginAdmin_required
def add_showtimes():
    form = ShowtimeForm()
    if request.method == 'POST' and form.validate_on_submit():
        fecha = escape(request.form['showtimeDate'])
        horario = escape(request.form['showtimeSchedule'])
        sala = escape(request.form['showtimeHall'])
        numSillas = escape(request.form['showtimeSeats'])
        pelicula = escape(request.form['showtimeMovie'])
        estatus = escape(request.form['showtimeStatus'])
        showtime = Screening(date=fecha, time=horario, number_seats=numSillas, movie_id=pelicula, movie_hall=sala, status=estatus)
        db.session.add(showtime)
        db.session.commit()
        return redirect(url_for('admin.list_showtimes'))
    return render_template('add_showtimes.html', form=form)


# Editar Funciones
@admin.route('/showtimes/edit/<int:id>', methods=["GET", "POST"])
@loginAdmin_required
def edit_showtime(id=None):
    form = ShowtimeForm()
    show = Screening.query.get_or_404(id)
    if request.method == 'GET':
        form.showtimeDate.data = show.date
        form.showtimeSchedule.data = show.time
        form.showtimeHall.data = show.movie_hall
        form.showtimeSeats.data = show.number_seats
        form.showtimeMovie.data = show.movie_id
        form.showtimeStatus.data = show.status
    if form.validate_on_submit():
        data = form.data
        show.date = data['showtimeDate']
        show.time = data['showtimeSchedule']
        show.movie_hall = data['showtimeHall']
        show.number_seats = data['showtimeSeats']
        show.movie_id = data['showtimeMovie']
        show.status = data['showtimeStatus']
        db.session.add(show)
        db.session.commit()
        return redirect(url_for('admin.list_showtimes'))
    return render_template('edit_showtime.html', form=form, fun=id)


# Eliminar Funciones TO DO: agregar warning
@admin.route('/showtimes/del/<int:id>/', methods=["GET", "POST"])
@loginAdmin_required
def delete_showtime(id):
    show = Screening.query.filter_by(screening_id=id).first_or_404()
    db.session.delete(show)
    db.session.commit()
    return redirect(url_for('admin.list_showtimes'))


@admin.route('/users/', methods=["GET", "POST"])
@loginAdmin_required
def list_users():
    users = User.query.filter_by(role = 'user').all()
    return render_template('list_users.html', users=users)

# Listado usuarios administrativos
@admin.route('/users-admin/', methods=["GET", "POST"])
@loginAdmin_required
@loginSuper_required
def list_admins():
    users = User.query.filter_by(role = 'admin').all()    
    return render_template('list_admins.html', users=users)

# Agregar usuarios administrativos
@admin.route('/users-admin/add/', methods=["GET", "POST"])
@loginAdmin_required
@loginSuper_required
def add_admins():
    form = AdminForm()
    if request.method == 'POST' and form.validate_on_submit():
        usuario = escape(request.form['userID'])
        nombre = escape(request.form['userName'])
        apellido = escape(request.form['userLastName'])
        correo = escape(request.form['userEmail'])
        telefono = escape(request.form['userPhone'])
        passw = escape(request.form['userPassword'])
        passwConf = escape(request.form['userPasswordConfirm'])
        status = escape(request.form['userStatus'])
        
        passw = SALT + passw + correo
        passw = generate_password_hash(passw)
        
        user = User(user_id=usuario, name=nombre, lastname=apellido, email=correo, celNum=telefono, password=passw, role='admin', status=status)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('admin.list_admins'))    
    return render_template('add_admins.html', form=form)


@admin.route('/bookings/', methods=["GET", "POST"])
@loginAdmin_required
def bookings():
    reservas = Booking.query.all()
    return render_template('bookings.html', reservas=reservas)
