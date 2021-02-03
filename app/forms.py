from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, ValidationError
from app.models import Pokedata


class pokedatabaseforms(FlaskForm):
    poke_id = IntegerField('poke_id', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    poketype = StringField('poketype', validators=[DataRequired()])
    submit = SubmitField('Enter Pokemon')

class caughtforms(FlaskForm):
    pokeball_id = IntegerField('pokeball_id', validators=[DataRequired()])
    nickname = StringField('Nickname', validators=[DataRequired()])
    submit = SubmitField('Enter Pokemon')


