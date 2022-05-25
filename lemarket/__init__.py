from flask import Flask
from flask_sqlalchemy import SQLAlchemy
webapp = Flask(__name__) 
webapp.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
webapp.config['SECRET_KEY'] = 'be52609c0bd9df4c2ae7f0f6'
db = SQLAlchemy(webapp)
from lemarket import routes
