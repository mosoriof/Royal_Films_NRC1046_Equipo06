from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, SelectField
from wtforms.validators import DataRequired, Email


class LoginForm(FlaskForm):
    user = StringField(
        "Usuario/Correo", validators=[DataRequired(message='Este campo es obligatorio'), Email(message='Dirección de correo electrónico inválida')])
    password = PasswordField("Contaseña", validators=[
                             DataRequired(message='Este campo es obligatorio')])
    remember_me = BooleanField("Recordarme", default=False)
    submit = SubmitField("Ingresar")


class SignupForm(FlaskForm):
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
    acceptConditions = BooleanField(
        "Acepto los términos y condiciones y políticas de protección de datos", default=False)
    submit = SubmitField("Crear cuenta")
