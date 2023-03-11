from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

#database instance with SQLALCHEMY
db = SQLAlchemy()
#Marshmallow instance
ma = Marshmallow()

def create_app():
    app = Flask(__name__)

    # establish the connection                 dbms                  db_user     pwd    URI      PORT  db_name
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://@localhost:5432/financing_database"

    # register blueprints
    from commands import db_commands
    app.register_blueprint(db_commands)

    # initialize extensions
    db.init_app(app)
    ma.init_app(app)
     # create the tables
    with app.app_context():
        db.create_all()

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)