from flask import render_template, request, redirect, url_for, flash
from app.forms import pokedatabaseforms
from app.models import  Pokedata
from app import app, db

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html")

headings = ("Poke_ID","Name","Poketype")
table=Pokedata.query.all()
print(table)




@app.route('/pokemondatabase', methods = ['GET', 'POST'])
def pokemondatabase():

    return render_template("pokemondatabase.html", table=table, headings=headings)

@app.route('/insert', methods = ['GET', 'POST'])
def insertpokemon():
    form = pokedatabaseforms()
    if form.validate_on_submit():
        pokemon = Pokedata( poke_id=form.poke_id.data, name=form.name.data, poketype=form.poketype.data)
        db.session.add(pokemon)
        db.session.commit()
        return redirect(url_for('pokemondatabase'))
    return render_template("insert.html", form=form)


@app.route('/catchpokemon')
def catchpokemon():
    return render_template("catchpokemon.html")
