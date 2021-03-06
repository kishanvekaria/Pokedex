from flask import render_template, request, redirect, url_for
from application.forms import pokedatabaseforms, caughtforms, rename
from application.models import  Pokedata, Caught
from application import app, db
import random
from sqlalchemy import func

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html")

headings = ("ID","Poke_ID","Name","Poketype",)

@app.route('/pokemondatabase', methods = ['GET', 'POST'])
def pokemondatabase():
    table = Pokedata.query.all()
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

headings_2 = ("ID","Pokeball_ID","Nickname","Update", "Delete")

@app.route('/catchpokemon', methods = ['GET', 'POST'])
def catchpokemon():
    headings_2 = ("ID", "Pokeball_ID", "Nickname", "Update", "Delete")
    table_2 = Caught.query.all()
    ball = Caught.id
    return render_template("catchpokemon.html", headings_2=headings_2, table_2 =table_2, ball=ball)

@app.route('/catchit', methods = ['GET', 'POST'])
def catchit():
    maxi = Pokedata.query.count()
    rand_num = random.randint(1, maxi)
    rand_poke = str(Pokedata.query.filter_by(id=rand_num).first())
    rand_list = rand_poke.split()
    rand_final = (rand_list[2] + ", Pokenumber#" + str(rand_list[1]) + ", " +  "ID is " + str(rand_list[0]))
    form = caughtforms()
    if form.validate_on_submit():
        ball = Caught( pokeball_id=form.pokeball_id.data, nickname=form.nickname.data, poke_name=Pokedata.query.filter_by(id=rand_list[0]).first())
        db.session.add(ball)
        db.session.commit()
        return redirect(url_for('catchpokemon'))
    return render_template("catchit.html", form=form, rand_final=rand_final,)


@app.route('/delete/<int:ball_id>', methods = ['GET', 'POST'])
def delete(ball_id):
    letitgo = Caught.query.filter_by(id=ball_id).first()
    db.session.delete(letitgo)
    db.session.commit()
    return redirect(url_for('catchpokemon'))


@app.route('/update/<int:ball_id>', methods = ['GET', 'POST'])
def update(ball_id):
    form = rename()
    if form.validate_on_submit():
        ballupdate = db.session.query(Caught).filter_by(id=ball_id).one()
        ballupdate.nickname= form.nickname.data
        db.session.commit()
        return redirect(url_for('catchpokemon'))
    return render_template('update.html', form=form )
