from flask import Flask, Response
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:password@localhost/sportsAlarm"
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from app import routes