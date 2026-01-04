# Application factory
from flask import Flask
from src.config import config

def create_app(config_name='default'):
    app = Flask(__name__)
    
    # Load config
    app.config.from_object(config[config_name])
    
    # Register Blueprints
    from src.blueprints.routes import health_check
    app.register_blueprint(health_check, url_prefix='/')


    
    return app