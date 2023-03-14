# Import Flask, SQLAlchemy, Marshmallow, and Bcrypt
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt

# Create global instances of SQLAlchemy, Marshmallow, and Bcrypt
db = SQLAlchemy()
ma = Marshmallow()
bcrypt = Bcrypt()

# Define the create_app() function to initialize the Flask application
def create_app():
    # Create a Flask application instance
    app = Flask(__name__)

    # Load the configuration settings from the app_config module
    app.config.from_object("config.app_config")
    
    # Initialize the SQLAlchemy, Marshmallow, and Bcrypt extensions
    db.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)

    # Register the db_commands blueprint for database management commands
    from commands import db_commands
    app.register_blueprint(db_commands)
    
    # Register each controller blueprint defined in registerable_controllers
    from controllers import registerable_controllers
    for controller in registerable_controllers:
        app.register_blueprint(controller)

    # Return the fully-configured Flask application instance
    return app

# If this script is run directly, create and run the Flask app
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)


