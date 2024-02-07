from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from flask_login import LoginManager
from flask_cors import CORS

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'asdf234askjhv235'
CORS(app)

login_manager = LoginManager()
login_manager.init_app(app)

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(app, model_class=Base)

from main import routes
