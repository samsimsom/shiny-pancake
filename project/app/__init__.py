

from flask import Flask


def create_app():
    app = Flask(__name__)

    # Blueprint Registration
    from app.main import main
    app.register_blueprint(main)

    return app
