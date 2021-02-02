from app import db

class Pokedata(db.Model):
    id = db.Column(db.Integer, primary_key =True)
    poke_id = db.Column(db.Integer)
    name = db.Column(db.String(30))
    poketype = db.Column(db.String(30))

    def __init__(self, id, poke_id,name,poketype):
        self.id = id
        self.poke_id = poke_id
        self.name =  name
        self.poketype = poketype
