import mysql.connector

conexion = mysql.connector.connect(

user = "root", password ="fenix7200",
host="localhost",
database="videojuegosmodels",
port="3306",)

print(conexion)

miCursor = conexion.cursor()

miCursor.execute("SELECT * FROM videojuegos WHERE ID = 1")

consulta = miCursor.fetchall()

fichero = open("archivo.txt","r+")

fichero.writelines("DATOS EXTRAIDOS % s"%consulta)

fichero.close

print(consulta)