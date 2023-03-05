from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

#CONFIG area
app = Flask(__name__)

#establish the connection                 dbms                  db_user     pwd    URI      PORT  db_name
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://@localhost:5432/financing_database"

#database instance with SQLALCHEMY
db = SQLAlchemy(app)
#Marshmallow instance
ma = Marshmallow(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'



if __name__ == '__main__':
    app.run(debug=True)