from flask_jwt_extended import JWTManager
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()
ma = Marshmallow()


def init_extension(app):
    db.init_app(app)
    jwt.init_app(app)
    ma.init_app(app)
    migrate.init_app(app)
