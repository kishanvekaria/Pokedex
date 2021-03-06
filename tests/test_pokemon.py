import unittest
from flask_testing import TestCase
from flask import url_for,render_template, request
import random                                                       

from application import app, db
from application.models import Pokedata, Caught
from application.forms import pokedatabaseforms, caughtforms, rename

class TestBase(TestCase):
    def create_app(self):

        app.config.update(SQLALCHEMY_DATABASE_URI="mysql+pymysql://qatraining:password@localhost/poketesting", SECRET_KEY='hello', TESTING = True,
        WTF_CSRF_ENABLED = False)
        return app
        

    def setUp(self):
        db.create_all()

        # sample data for database
        poke = Pokedata(id=1, poke_id=1, name='Bulbasaur', poketype='Grass')
        db.session.add(poke)
        db.session.commit()
        poke_2 = Pokedata(id=2, poke_id=2, name='Ivysaur', poketype='Grass')
        db.session.add(poke_2)
        db.session.commit()
        caughtpoke = Caught(id=1, poke_id=1, nickname='Bulba', data_id=1)
        db.session.add(caughtpoke)
        db.session.commit()
        caughtpoke_2 = Caught(id=2, pokeball_id=2, nickname='Ivy', data_id=2)
        db.session.add(caughtpoke_2)
        db.session.commit()

    def tearDown(self):
        db.drop_all()

class TestAccess(TestBase):
    def test_access_home(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

    def test_access_pokemondatabase(self):
        response = self.client.get(url_for('pokemondatabase'))
        self.assertEqual(response.status_code, 200)

    def test_access_insertpokemon(self):
        response = self.client.get(url_for('insertpokemon'))
        self.assertEqual(response.status_code, 200)

    def test_access_catchpokemon(self):
        response = self.client.get(url_for('catchpokemon'))
        self.assertEqual(response.status_code, 200)

    def test_access_catchit(self):
        response = self.client.get(url_for('catchit'))
        self.assertEqual(response.status_code, 200)

class TestAccessupdate(TestBase):
    def test_access_update(self):
        response = self.client.get(url_for('update', ball_id= 2))
        self.assertEqual(response.status_code, 200)

class TestAccessdelete(TestBase):
    def test_access_delete(self):
        response = self.client.get(url_for('delete', ball_id=1))
        self.assertEqual(response.status_code, 200)

class TestRead(TestBase):
    def test_find_poke(self):
        response = self.client.get(url_for('pokemondatabase'))
        self.assertIn(b'Bulbasaur', response.data)

class Testform(TestBase):
    def test_form(self):
        response = self.client.post((url_for('insertpokemon')),
                                        data=dict(poke_id=1, name="Bulbasaur", poketype='Grass'),follow_redirects=True)
        self.assertIn(b'Welcome to the Pokedex Database', response.data)




