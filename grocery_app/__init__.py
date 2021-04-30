from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from grocery_app.config import Config
import os
from flask_bcrypt import Bcrypt 

app = Flask(__name__)
app.config.from_object(Config)
app.secret_key = os.urandom(24)


db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
from grocery_app.routes import main, auth


app.register_blueprint(main)

app.register_blueprint(auth)  # registered auth blueprint

with app.app_context():
    db.create_all()



# Authentication
from flask_login import LoginManager
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

from .models import User


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)



