from flask import render_template
from app import app

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/pokemondatabase')
def pokemondatabase():
    return render_template("pokemondatabase.html")

@app.route('/catchpokemon')
def catchpokemon():
    return render_template("catchpokemon.html")