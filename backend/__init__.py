from flask import Flask

from .extensions.routes import register_routes


def create_app():
    app = Flask(
        __name__,
        static_folder='../frontend/static',
        template_folder='../frontend/templates', )

    register_routes(app)    
    
    return app