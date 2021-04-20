
import os
from flask import Flask
from config import DevelopmentConfig


def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)

    # Blueprint Registration
    from app.main import main
    app.register_blueprint(main)

    return app
