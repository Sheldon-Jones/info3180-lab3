from flask import Flask
from flask_mail import Mail 
from .config import Config

secretkey='Som3$ec5etK*y'
app = Flask(__name__)
app.config.from_object(Config) 
mail = Mail(app)
from app import views



