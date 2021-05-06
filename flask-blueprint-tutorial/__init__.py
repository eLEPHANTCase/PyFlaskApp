""" Initialize Flask App """
from flask import Flask
from flask_assets import Environment # <- `Environment`?

def create_app():
    """ Create Flask Application """
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')
    assets = Environment() # Create an assets environment
    assets.init_app(app) # Initialize Flask-Assets

    with app.app_context():
        # Import Parts of Our Application
        from .profile import routes
        from .home import routes
        from .products import routes
        from .assets import compile_static_assets

        # Register Blueprints
        app.register_blueprint(profile.account_bp)
        app.register_blueprint(home.home_bp)
        app.register_blueprint(products.product_bp)

        # Compile Static Assets
        compile_static_assets(assets) # Execute Logic

        return app