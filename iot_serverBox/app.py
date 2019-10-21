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
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()