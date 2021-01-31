from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from wtforms import StringField, SubmitField, IntergerField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SECRET_KEY'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"

db = SQLAlchemy(app)

class Pokedata(db.Model):
    id = db.Column(db.Integer, primary_key =True)
    poke_id = db.Column(db.Integer)
    name = db.Column(db.String(30))
    poketype = db.Column(db.String(30))

    def __init__(self,poke_id,name,poketype):
        self.poke_id = poke_id
        self.name =  name
        self.poketype = poketype

from app import routes, models