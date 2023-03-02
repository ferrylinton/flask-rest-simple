from .error import error_handlers

def register_routes(app):
    
    from .main import main as main_blueprint
    from .user import user as user_blueprint

    app.register_blueprint(main_blueprint)
    app.register_blueprint(user_blueprint, url_prefix='/api/users')

    error_handlers(app)