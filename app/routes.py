from flask import render_template, request, redirect, url_for, flash
from app.forms import pokedatabaseforms
from app import app

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/pokemondatabase', methods = ['GET', 'POST'])
def pokemondatabase():
    form = pokedatabaseforms()
    return render_template("pokemondatabase.html", form = form)

@app.route('/insert', methods = ['GET', 'POST'])
def insertpokemon():
    form = pokedatabaseforms()
    if form.validate_on_submit():
        return redirect(url_for('pokemondatabase'))
    return render_template("insert.html", form=form)


@app.route('/catchpokemon')
def catchpokemon():
    return render_template("catchpokemon.html")
