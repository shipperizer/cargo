from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.migrate import Migrate

db = SQLAlchemy()


def init_database(app):
    db.init_app(app)
    migrate = Migrate(app, db)
