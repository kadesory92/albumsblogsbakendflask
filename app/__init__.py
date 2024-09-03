import os

from flask import Flask
from .config import config_by_name
from .extensions import db, migrate, jwt, ma


def create_app(config_name='development'):
    app = Flask(__name__)
    # app.config.from_object(config_by_name[config_name])
    app.config.from_object(config_by_name[os.getenv('FLASK_ENV', 'development')])

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    ma.init_app(app)

    # Register blueprints
    from .controllers import register_blueprints
    register_blueprints(app)

    return app

