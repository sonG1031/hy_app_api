from flask import Flask
from flask_restx import Api
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


import config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    #ORM
    db.init_app(app)
    migrate.init_app(app, db)
    from . import models
    api = Api(app)

    #namespace
    from .route.auth import auth
    api.add_namespace(auth, '/auth')



    return app