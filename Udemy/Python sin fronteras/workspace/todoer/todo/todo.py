from todo.auth import login_required
from todo.db import get_db
from werkzeug.exceptions import abort
from flask import (
    url_for, redirect, request, render_template, Blueprint, g, flash
)

bp = Blueprint('todo', __name__)

@bp.route('/')
@login_required
def index():
    db, c = get_db()
    c.execute(
        """
            SELECT t.id, t.description, t.completed, t.created_at, u.username
            FROM todo t
            JOIN user u
            ON t.created_by = u.id
            WHERE u.id = %s
            ORDER BY created_at DESC
        """,
        (g.user['id'],)
    )
    todos = c.fetchall()

    return render_template('todo/index.html', todos=todos)

@bp.route('/create', methods=['GET','POST'])
@login_required
def create():
    if request.method == 'POST':
        description = request.form['description']
        completed = True if request.form['completed'] == "1" else False
        error = None

        if description is None:
            error = 'Description required'
        if error is not None:
            flash(error)
        else:
            db, c = get_db()
            c.execute(
            """
                INSERT INTO todo (description, completed, created_by)
                values (%s, %s, %s)
            """,
            (description, completed, g.user['id'])
            )
            db.commit()
            return redirect(url_for('todo.index'))

    return render_template('todo/create.html')

@bp.route('/<int:id>/update', methods=['GET','POST'])
@login_required
def update(id):

    def getTodo():
        db, c = get_db()
        c.execute(
        """
            SELECT id, description, completed, created_at, created_by
            FROM todo
            WHERE id = %s
            AND created_by = %s
        """,
        (id,g.user['id'])
        )
        return c.fetchone()

    if request.method == 'GET':

        todo = getTodo()

        if todo is None:
            abort(400,'Todo {0} not found or user does not have permission to access'.format(id))

        return render_template('todo/update.html', todo=todo)

    elif request.method == 'POST':
        description = request.form['description']
        completed = True if request.form.get('completed') == "on" else False
        error = None

        if None in [description, completed]:
            error = "necessary data not found"
        if error is not None:
            flash(error)
        else:
            db, c = get_db()
            c.execute(
                """
                    UPDATE todo
                    SET description=%s, completed=%s
                    WHERE id = %s
                """,
                (description, completed, g.user['id'])
            )
            db.commit()
        return render_template('todo/update.html', todo=getTodo())

@bp.route('/<int:id>/delete', methods=['POST'])
@login_required
def delete(id):
    db, c = get_db()
    error = None
    c.execute(
    """
        DELETE FROM todo
        WHERE id = %s
        AND created_by = %s
    """,
    (id,g.user['id'])
    )

    if c.rowcount == 0:
        error = "Error deleting the {0} Todo".format(id)
    if error is not None:
        abort(400,error)
    else:
        db.commit()
        return redirect(url_for('todo.index'))