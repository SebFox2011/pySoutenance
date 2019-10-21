from app import db
from datetime import datetime

class EventEmitter(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    idEmetteur = db.Column(db.String(7), nullable=False)
    typeEvenement = db.Column(db.String(10), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

event1 = EventEmitter(idEmetteur="id00000",typeEvenement='ouverture')
event2 = EventEmitter(idEmetteur="id00001",typeEvenement='ouverture')
db.session.add(event1)
db.session.add(event2)
db.session.commit()