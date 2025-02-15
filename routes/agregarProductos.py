from flask import Flask, session, request, redirect, url_for, render_template , Blueprint
from flask_mysqldb import MySQL
import secrets
import os
import base64
import bcrypt
from werkzeug.utils import secure_filename
import MySQLdb

app = Flask(__name__)
agregar = Blueprint('agregarP', __name__)
try:
    mysql = MySQLdb.connect(
        host="bogk9mha8ehn5owk1qeo-mysql.services.clever-cloud.com",
        user="udq78qvouupy05hi",
        passwd="FjhgEsSoU9KepA4XgIxR",
        db="bogk9mha8ehn5owk1qeo"
    )
    
except MySQLdb.Error as e:
    print(f"Error al conectar: {e}")
@app.route("/agregarProducto", methods=['GET', 'POST'])
def agregarProducto():
    if request.method == 'POST':
        nombre = request.form['nombre']
        marca = request.form['marca']
        referencia = request.form['referencia']
        color = request.form['color']
        precioB = request.form['precioB']
        precioF = request.form['precioF']
        stock = request.form['stock']
        
        cursor = mysql.cursor()
        cursor.execute('INSERT INTO Productos (NOMBRE,MARCA,REFERENCIA) VALUES (%s, %s , %s)',(nombre,marca,referencia))
        mysql.commit()
        cursor = mysql.cursor()
        cursor.execute('SELECT ID_Producto FROM Productos ORDER BY ID_Producto DESC LIMIT 1')
        id = cursor.fetchone()
        cursor.close()
        cursor = mysql.cursor()
        cursor.execute('INSERT INTO Detalles_Producto (ID_Producto,Color,Precio_Base,Precio_Final,Stock) VALUES (%s, %s , %s, %s, %s)',(id,color,precioB,precioF,stock))
        mysql.commit()
        return redirect(url_for('productos_route'))
    else:
        print("ERROR")

