import functools
from werkzeug.security import check_password_hash, generate_password_hash
from todo.db import get_db
from flask import (
    session, request, redirect, url_for, g, Blueprint, render_template, flash
)

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db, c = get_db()
        error = None
        c.execute(
            'select id from user where username = %s',
            (username,)
        )
        if not username:
            error = 'Username required'
        if not password:
            error = 'Password required'
        elif c.fetchone() is not None:
            error = 'Usuario {} se encuentra registrado'.format(username)
        if error is None:
            print(generate_password_hash(password))
            c.execute(
                'insert into user(username, password) values(%s,%s)',
                (username, generate_password_hash(password))
            )
            db.commit()
            return redirect(url_for('auth.login'))

        flash(error)

    return render_template('auth/register.html')

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db, c = get_db()
        error = None
        c.execute(
            'select id, password from user where username = %s',
            (username,)
        )
        user = c.fetchone()

        if user is None:
            error = 'User or pasword is invalid'
        elif not check_password_hash(user['password'], password):
            error = 'User or pasword is invalid'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('todo.index'))

        flash(error)

    return render_template('auth/login.html')

@bp.before_app_request
def load_logger_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        db, c = get_db()
        c.execute(
            'select * from user where id = %s',
            (user_id,)
        )
        g.user = c.fetchone()

def login_required(view): #Funcion decoradora
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.get('user') is None:
            return redirect(url_for('auth.login'))
        return view(**kwargs)

    return wrapped_view

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for(login))