from .error import error_handlers

def register_routes(app):
    
    from .user_controller import blueprint as user_blueprint
    app.register_blueprint(user_blueprint, url_prefix='/api/users')

    error_handlers(app)