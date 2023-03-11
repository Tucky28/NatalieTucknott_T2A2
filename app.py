from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
ma = Marshmallow()
bcrypt = Bcrypt()

def create_app():

    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://@localhost:5432/financing_database"
    
    db.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)

    from commands import db_commands
    app.register_blueprint(db_commands)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)





