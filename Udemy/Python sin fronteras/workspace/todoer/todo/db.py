import click
from mysql import connector
from flask import current_app, g
from .schema import instructions
from flask.cli import with_appcontext

def get_db():
    if 'db' not in g:
        g.db = connector.connect(
            host=current_app.config['DATABASE_HOST'],
            user=current_app.config['DATABASE_USER'],
            password=current_app.config['DATABASE_PASSWORD'],
            database=current_app.config['DATABASE']
        )
        g.c = g.db.cursor(dictionary=True)
    return g.db, g.c


def init_db():
    db, c = get_db()

    for i in instructions:
        c.execute(i, multi=True)

    db.commit()

@click.command('init-db')
@with_appcontext
def init_db_command():
    init_db()
    click.echo('DB initialized')

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)