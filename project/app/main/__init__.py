

from flask import Blueprint

main = Blueprint('main', __name__, url_prefix='/')


def load_routes():
    from app.main import routes


load_routes()
