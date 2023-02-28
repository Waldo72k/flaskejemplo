#python3 -m venv virtual
#source virtual/bin/activate
#flask --app app run

from flask import Flask
import mysql.connector

conexion = mysql.connector.connect(

user = "root", password ="fenix7200",
host="localhost",
database="videojuegosmodels",
port="3306",)

print(conexion)

miCursor = conexion.cursor()

miCursor.execute("SELECT * FROM videojuegos WHERE ID = 2")

consulta = miCursor.fetchall()

app = Flask(__name__)

@app.route("/")
def main():
    return "<h1><center>HOLA ITE Ensenada</center></h1><marquee>% s</marquee>"%consulta

@app.route("/bye")
def adios():
    return "bye bye"

#flask --app app run --port=80 <-asi se arranca el api, desde la virtualizacion