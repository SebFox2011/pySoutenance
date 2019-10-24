# Projet de soutenance - Boite aux lettres connectée

## Description du projet

Le but du projet est de détecter l'ouverture de la boite aux lettres et d'envoyer un signal pour indiquer son ouverture en enregistrant sur un server web, l'id de l'émetteur ainsi que la date et l'heure de l'événement. Les informations du server sont stockées in-situ sur une base de données sqlite

## Organisation

Pour réaliser ce projet 2 rapsberry seront utilisés :
    - iot_letterBox: Emetteur
        Détécte l'événement d'ouverture de la boite aux lettres via un capteur de luminosité et envoi via une méthode post l'information au server.
    - iot_serverBox: Récepteur
        Gère une interface web de présentation des données, met à disposition une api et indique par un signal sonore que l'émétteur a envoyé un signal.

## Réalisation
Réalisation V1 du projet: 
l'émetteur envoi un signal à l'ouverture de la boite avec les informations suivantes:
identifiant : idXXXXX : XXXXX nombre compris entre 00001 et FFFFF
Date et heure 
type d'événement : open

Le récépteur met à disposition une api (get / post) et enregistre les données en bdd sur sqlite. 
Il émet un signal sonore à chaque ouverure de la boite aux lettres


Réalisation V2 du projet: 
Le server envoi une notification mail à l'utilisateur dont l'adresse mail est renseignée. Il peut aussi  recoir une notification.


## Utilisation

Pour le server iot_serverBox:
Buzzer / led connecté sur la broche BCM14

Mise ne place de l'environ

    sudo apt-get install python3-venv (si pas déjà installé)

    python3 -m venv venv

    . venv/bin/activate
    
    pip install Flask (si pas déjà installé)

    export FLASK_APP=application.py 

    flask run --host=0.0.0.0

Installation et configuration de la base donnée:

pip install Flask-SQLAlchemy

pip install Flask-Migrate

flask db init

flask db migrate

flask db upgrade

Puis ensuite mettre les jeux de données de test

pour utiliser les GPIO:

pip install RPi.GPIO

pour twitter:

pip install twython
https://twython.readthedocs.io/en/latest/

Pour le server iot_letterBox:
python3 application.py

Capteur de luminosité connecté sur la broche BCM4
