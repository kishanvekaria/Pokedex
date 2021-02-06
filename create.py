from app import db
from app.models import Pokedata, Caught

db.drop_all()
db.create_all()

