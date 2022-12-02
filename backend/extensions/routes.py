from ..controllers import home_controller


def register_routes(app):
    routes = [
        home_controller.home
    ]

    for route in routes:
        app.register_blueprint(route)