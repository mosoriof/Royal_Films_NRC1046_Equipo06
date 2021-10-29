from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, SelectField, TextAreaField, SelectMultipleField
from wtforms.validators import DataRequired, Email
from wtforms import validators

genreList=[('Acción', 'Acción'), ('Animada', 'Animada'), ('Ciencia Ficción', 'Ciencia Ficción'), ('Comedia', 'Comedia'), ('Drama', 'Drama'), ('Infantil', 'Infantil'), ('Musical', 'Musical'), ('Romance', 'Romance'), ('Terror', 'Terror')]


scheduleList=[('1', '1:50 PM - 5:30 PM - 9:10 PM'), ('2', '11:40 PM - 3:00 PM - 6:20 PM - 9:40 PM'), ('3', '2:10 PM - 5:00 PM - 7:50 PM'), ('4', '11:20 AM - 2:10 PM - 5:00 PM - 7:50 PM'), ('5', '2:50 PM - 6:00 PM - 9:00 PM'), ('6', '2:00 PM - 4:50 PM - 8:00 PM'), ('7', '11:50 AM - 2:50 PM - 6:00 PM - 9:00 PM'), ('8', '3:00 PM - 5:50 PM - 8:50 PM')]

hallList=[('1', 'Sala 1'), ('2', 'Sala 2'), ('3', 'Sala 3'), ('4', 'Sala 4'), ('5', 'Sala 5')]

statusList=[('new', 'new'), ('active', 'active'), ('inactive', 'inactive')]
class LoginAdminForm(FlaskForm):
    user = StringField(
        "Usuario/Correo", validators=[DataRequired(message='Este campo es obligatorio'), Email(message='Dirección de correo electrónico inválida')])
    password = PasswordField("Contaseña", validators=[
                             DataRequired(message='Este campo es obligatorio')])
    # remember_me = BooleanField("Recordarme", default=False)
    submit = SubmitField("Ingresar")


class MovieForm(FlaskForm):
    movieTitle = StringField("Título", validators=[
                             DataRequired(message='Este campo es obligatorio')])
    moviePoster = StringField("Poster", validators=[
                              DataRequired(message='Este campo es obligatorio')])
    movieTrailer = StringField("Trailer", validators=[
                               DataRequired(message='Este campo es obligatorio')])
    movieSynopsis = TextAreaField("Sinopsis", validators=[
                                DataRequired(message='Este campo es obligatorio')])
    movieLength = StringField("Duración", validators=[
                              DataRequired(message='Este campo es obligatorio')])
    movieFormat = SelectField("Formato", choices=[(
        '2D - Subtítulado', '2D - Subtítulado'), ('2D - Doblado', '2D - Doblado'), ('3D - Subtítulado', '3D - Subtítulado'), ('3D - Doblado', '3D - Doblado')])
    movieGenre = SelectField("Género", choices=genreList)
    movieRating = SelectField("Clasificación", choices=[('Todos', 'T'), ('Mayores de 7 años', '7-A'), ('Mayores de 12 años', '12-A'), ('Mayores de 15 años', '15-A'), ('Mayores de 18 años', '18-A' )])
    movieCast = StringField(
        "Cast", validators=[DataRequired(message='Este campo es obligatorio')])
    movieRelease = StringField("Estreno", validators=[
        DataRequired(message='Este campo es obligatorio')])
    movieStatus = SelectField("Status", choices=statusList)
    
    submit = SubmitField("Aceptar")

class ShowtimeForm(FlaskForm):
    showtimeDate = StringField("Fecha", validators=[DataRequired(message='Este campo es obligatorio')])
    showtimeSchedule = SelectField("Horario", choices=scheduleList)
    showtimeHall = SelectField("Sala", choices=hallList)
    showtimeSeats = StringField("Número Tiquetes", validators=[DataRequired(message='Este campo es obligatorio')])
    showtimeMovie = StringField("Película", validators=[DataRequired(message='Este campo es obligatorio')])
    showtimeStatus = SelectField("Status", choices=[('active', 'active'), ('inactive', 'inactive')]) 
    submit = SubmitField("Aceptar")
    


class AdminForm(FlaskForm):
    userID = StringField("Número de documento", validators=[
                         DataRequired(message='Este campo es obligatorio')])
    userName = StringField("Nombre", validators=[
                           DataRequired(message='Este campo es obligatorio')])
    userLastName = StringField("Apellidos", validators=[
                               DataRequired(message='Este campo es obligatorio')])
    userPhone = StringField("Celular", validators=[
                            DataRequired(message='Este campo es obligatorio')])
    userEmail = StringField("Correo electrónico", validators=[DataRequired(
        message='Este campo es obligatorio'), Email(message='Dirección de correo electrónico inválida')])
    userPassword = PasswordField("Contraseña", validators=[
                                 DataRequired(message='Este campo es obligatorio')])
    userPasswordConfirm = PasswordField("Confirmar contraseña", validators=[
                                        DataRequired(message='Este campo es obligatorio')])
    userStatus = SelectField("Status", choices=[('active', 'active'), ('inactive', 'inactive')]) 
    submit = SubmitField("Aceptar")
    