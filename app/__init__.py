from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail
# from flask_bcrypt import Bcrypt



app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
mail = Mail(app)

# bcrypt = Bcrypt(app)

from app import routes, models