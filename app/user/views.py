from flask import render_template, session, redirect, url_for
import functools

from . import user


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if 'usuario' not in session:
            return redirect(url_for('home.login'))
        return view(**kwargs)

    return wrapped_view


@user.route('/', methods=["GET", "POST"])
@login_required
def perfil():
    user = "true"
    infoUser = session['nombre']
    return render_template('perfil.html', user=user, infoUser=infoUser)


@user.route('/comentarios', methods=["GET", "POST"])
@login_required
def comentarios():
    user = "true"
    infoUser = session['nombre']
    return render_template('comentarios.html', user=user, infoUser=infoUser)


@user.route('/comentarios-new', methods=["GET", "POST"])
@login_required
def comentarios_new():
    user = "true"
    infoUser = session['nombre']
    return render_template('comentariosNew.html', user=user, infoUser=infoUser)


@user.route('/compras', methods=["GET", "POST"])
@login_required
def compras():
    user = "true"
    infoUser = session['nombre']
    return render_template('compras.html', user=user, infoUser=infoUser)


@user.route('/favoritos', methods=["GET", "POST"])
@login_required
def favoritos():
    user = "true"
    infoUser = session['nombre']
    return render_template('favoritos.html', user=user, infoUser=infoUser)


@user.route('/cambio', methods=["GET", "POST"])
@login_required
def cambioPass():
    user = "true"
    infoUser = session['nombre']
    return render_template('cambioPass.html', user=user, infoUser=infoUser)


@user.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home.login'))
