#python3 -m venv virtual
#source virtual/bin/activate
#flask --app app run

from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "HOLA ITE Ensenada"

@app.route("/bye")
def adios():
    return "bye bye"