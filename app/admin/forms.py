from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, SelectField, TextAreaField, SelectMultipleField
from wtforms.validators import DataRequired, Email
from wtforms import validators

genreList=[('A', 'Acción'), ('AN', 'Animada'), ('D', 'Drama'), ('C', 'Comedia'), (
        'I', 'Infantil'), ('T', 'Terror'), ('CF', 'Ciencia Ficción'), ('R', 'Romance'), ('M', 'Musical')]
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
        '2D-S', '2D-Subtítulado'), ('2D-D', '2D-Doblado'), ('3D-S', '3D-Subtítulado'), ('3D-D', '3D-Doblado')])
    movieGenre = SelectField("Género", choices=genreList)
    movieRating = SelectField("Clasificación", choices=[('Todos', 'T'), ('Mayores de 7 años', '7-A'), ('Mayores de 12 años', '12-A'), ('Mayores de 15 años', '15-A'), ('Mayores de 18 años', '18-A' )])
    movieCast = StringField(
        "Cast", validators=[DataRequired(message='Este campo es obligatorio')])
    movieRelease = StringField("Estreno", validators=[
        DataRequired(message='Este campo es obligatorio')])
    submit = SubmitField("Agregar")
