#python3 -m venv virtual
#source virtual/bin/activate
#flask --app app run

from flask import Flask, jsonify
import mysql.connector
import json

conexion = mysql.connector.connect(

user = "root", password ="fenix7200",
host="localhost",
database="videojuegosmodels",
port="3306",)

print(conexion)

miCursor = conexion.cursor()

miCursor.execute("SELECT * FROM videogames WHERE ID = 1")

consulta = miCursor.fetchall()

app = Flask(__name__)

@app.route("/")
def main():
    return "<h1><center>VGDb</center></h1>"
##Asi se declara un endpoint, en este caso es el /bye
@app.route("/videogames")
def videogames():
    miCursor.execute("SELECT * FROM videogames")
    data = []
    for row in miCursor:
        data.append(row)
    return jsonify(data)

@app.route("/developers")
def developers():
    miCursor.execute("SELECT * FROM developers")
    data = []
    for row in miCursor:
        data.append(row)
    return jsonify(data)

@app.route("/publishers")
def publishers():
    miCursor.execute("SELECT * FROM publishers")
    data = []
    for row in miCursor:
        data.append(row)
    return jsonify(data)

@app.route("/sql/test")
def testConsulta():
    return "<h1><center>Test de consulta de MySQL</center></h1><marquee>% s</marquee>"%consulta

@app.route("/about")
def about():
    with open("robots.json", "r") as f:
        index = json.load(f)
    return jsonify(index)

#flask --app app run --port=80 <-asi se arranca el api, desde la virtualizacion