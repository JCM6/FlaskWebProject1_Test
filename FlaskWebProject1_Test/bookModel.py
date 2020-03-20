from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json
from FlaskWebProject1_Test/settings.py import app
db = SQLAlchemy(app)

class Book(db.Model):
    __tablename__ = 'books'
    name = db.Column()
    
