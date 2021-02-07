from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, ValidationError
from application.models import Pokedata


class pokedatabaseforms(FlaskForm):
    poke_id = IntegerField('Poke_id', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    poketype = StringField('Poketype', validators=[DataRequired()])
    submit = SubmitField('Enter Pokemon')

class caughtforms(FlaskForm):
    pokeball_id = IntegerField('Pokeball_id', validators=[DataRequired()])
    nickname = StringField('Nickname', validators=[DataRequired()])
    refid = IntegerField('Enter ID above', validators=[DataRequired()])
    submit = SubmitField('Enter Pokemon')

class rename(FlaskForm):
    nickname = StringField('Nickname', validators=[DataRequired()])
    submit = SubmitField('Enter Pokemon')
