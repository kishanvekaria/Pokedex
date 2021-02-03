from flask import render_template, request, redirect, url_for, flash
from app.forms import pokedatabaseforms, caughtforms
from app.models import  Pokedata, Caught
from app import app, db
import random
from sqlalchemy import func

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html")

headings = ("ID","Poke_ID","Name","Poketype", "Update", "Delete")
table = Pokedata.query.all()
print(table)
pokemon=Pokedata.id

@app.route('/pokemondatabase', methods = ['GET', 'POST'])
def pokemondatabase():
    table = Pokedata.query.all()
    print(table)
    pokemon = Pokedata.id
    return render_template("pokemondatabase.html", table=table, headings=headings, pokemon=pokemon)

@app.route('/insert', methods = ['GET', 'POST'])
def insertpokemon():
    form = pokedatabaseforms()
    if form.validate_on_submit():
        pokemon = Pokedata( poke_id=form.poke_id.data, name=form.name.data, poketype=form.poketype.data)
        db.session.add(pokemon)
        db.session.commit()
        return redirect(url_for('pokemondatabase'))
    return render_template("insert.html", form=form)

maxi = Pokedata.query.count()
rand_num= random.randint(1,maxi)
headings_2 = ("ID","Pokeball_ID","Nickname","Update", "Delete")
table_2 = Caught.query.all()
print(table_2)
ball=Pokedata.id
@app.route('/catchpokemon')
def catchpokemon():
    return render_template("catchpokemon.html")

@app.route('/catchit')
def catchit():
    throw = caughtforms()
    if throw.validate_on_submit():
        ball = Caught( pokeball_id=throw.pokeball_id.data, nickname=throw.nickname.data,)
        db.session.add(ball)
        db.session.commit()
    return render_template("catchit.html", throw=throw)

@app.route('/delete')
def delete():
    return render_template("delete.html")

@app.route('/update')
def update():
    return render_template("update.html")