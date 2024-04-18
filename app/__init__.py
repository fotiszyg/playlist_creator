from flask import Flask

import list.views
import song.views
from config import load_config
from connect import connect
from database.extensions import db


def create_app():
    app = Flask(__name__)

    app.register_blueprint(song.views.bp)
    app.register_blueprint(list.views.bp)

    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:0000@localhost:5432/postgres"

    config = load_config()

    with app.app_context():
        connect(config)
        db.init_app(app)
        db.drop_all()
        db.create_all()

    return app
