from app import db

class Pokedata(db.Model):
    id = db.Column(db.Integer, primary_key =True)
    poke_id = db.Column(db.Integer)
    name = db.Column(db.String(30))
    poketype = db.Column(db.String(30))
    caught_pokemon = db.relationship('Caught', backref = 'poke_name')

    def __repr__(self):
        return f"{self.id} {self.poke_id} {self.name} {self.poketype}"

class Caught(db.Model):
    id = db.Column(db.Integer, primary_key =True)
    pokeball_id= db.Column(db.Integer)
    nickname = db.Column(db.String(30))
    data_id = db.Column(db.Integer, db.ForeignKey('pokedata.id'))

    def __repr__(self):
        return f"{self.data_id} {self.pokeball_id} {self.nickname}"
