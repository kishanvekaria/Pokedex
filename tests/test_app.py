import unittest
from flask_testing import TestCase
from flask import url_for

from app import app, db
from app.models import Pokedata, Caught

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///test", SECRET_KEY='hello')
        return app

    def setup(self):
        db.create_all()

        poke = Pokedata(id=1, poke_id=1, name='Bulba', poketype='Grass')
        db.session.add(poke)
        db.session.commit()
        #sample data for database


    def tearDown(self):
        db.drop_all()

class TestAccess(TestBase):
    def test_access_home(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

    def test_find_poke(self):

        response = self.client.get(url_for('pokedata'))
        self.assertIn(b'Bulba', response.data)


