from flask import Flask
from flask import render_template, request,redirect, url_for,jsonify  # jinja2
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
from flask_migrate import Migrate
from classes.buzzer import Buzzer
from classes.mail import envoiMail

app = Flask(__name__)

## création de la base données
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

##pour flask-migrate
migrate = Migrate(app, db)

from classes.evenements import EventEmitter

buzzer = Buzzer(14)

@app.route('/')
def index5():
    events= EventEmitter.query.order_by(desc(EventEmitter.created_at)).limit(5)
    return render_template('index.html',events=events)

@app.route('/event')
def indexAll():
    events= EventEmitter.query.all()
    return render_template('event.html',events=events)

@app.route('/event/delete/<int:id>')
def deleteEvent(id):
    event = EventEmitter.query.filter_by(id=id).first_or_404()# si jamais l'id n'existe pas
    db.session.delete(event)
    db.session.commit()
    return redirect(url_for('index5'))

@app.route('/event/add',methods=["POST"])
def addEvent():
    buzzer.bip(2)
    #event=True
    # crée un événement
    response = request.form
    idEmetteur = response['idEmetteur']
    typeEvenement = response['typeEvenement']
    print(idEmetteur +' '+ typeEvenement )
    # Création de l'événement
    event = EventEmitter(idEmetteur=idEmetteur, typeEvenement=typeEvenement)
    #enregistre en bdd
    db.session.add(event)
    db.session.commit()
    #envoiMail() # A travailler car l'envoi ne fonctionne pasq
    return redirect(url_for('index5',event=event))

if __name__ == '__main__':
    app.run()