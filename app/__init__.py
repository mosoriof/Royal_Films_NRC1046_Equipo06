from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/cinema.db'

app.secret_key = "|6KIb:nzTr-\5*me+S^G"

db = SQLAlchemy(app)

# Registro de los Blueprints
from .admin import admin
app.register_blueprint(admin, url_prefix='/admin')

from .home import home
app.register_blueprint(home)

from .user import user
app.register_blueprint(user, url_prefix='/perfil')


# app.secret_key = "|6KIb:nzTr-\5*me+S^G"

# SALT = 'BnM02I$#R7'
