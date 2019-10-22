from flask import Flask
from flask import render_template, request,redirect, url_for,jsonify  # jinja2
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

## création de la base données
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

##pour flask-migrate
migrate = Migrate(app, db)

from classes.evenements import EventEmitter


@app.route('/')
def index5():
    events= EventEmitter.query.limit(5)
    return render_template('index.html',events=events)

@app.route('/event')
def indexAll():
    events= EventEmitter.query.all()
    return render_template('index.html',events=events)

@app.route('/event/delete/<int:id>')
def deleteEvent(id):
    event = EventEmitter.query.filter_by(id=id).first_or_404()# si jamais l'id n'existe pas
    db.session.delete(event)
    db.session.commit()
    return redirect(url_for('index5'))

@app.route('/event/add',methods=["POST"])
def addEvent():
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
    return redirect(url_for('index5'))

if __name__ == '__main__':
    app.run()