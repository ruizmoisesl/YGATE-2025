from flask import Flask, session, request, redirect, url_for, render_template , Blueprint
import secrets
import os
import base64
import bcrypt
from werkzeug.utils import secure_filename
import mysql.connector as MySQLdb
from database import iniciar_connection

app = Flask(__name__)
agregar = Blueprint('agregar', __name__)
mysql = None

@agregar.route("/agregarProducto", methods=['GET', 'POST'])
def agregarProducto():
    conexion = iniciar_connection()
    cursor = conexion.cursor()
    print("######################!!!!!! ACABE DE ENTRAR A LA FUNCION 'AGREGARPRODUCTO'!!!!!!!!!!!#################### " )
    if request.method == 'POST':
        nombre = request.form['nombre']
        marca = request.form['marca']
        referencia = request.form['referencia']
        color = request.form['color']
        precioB = request.form['precioB']
        precioF = request.form['precioF']
        stock = request.form['stock']
        

        cursor.execute('INSERT INTO Productos (NOMBRE,MARCA,REFERENCIA) VALUES (%s, %s , %s)',(nombre,marca,referencia))
        conexion.commit()
        cursor.execute('SELECT ID_Producto FROM Productos ORDER BY ID_Producto DESC LIMIT 1')
        id = cursor.fetchone()[0]
        cursor.execute('INSERT INTO Detalles_Producto (ID_Producto,Color,Precio_Base,Precio_Final,Stock) VALUES (%s, %s , %s, %s, %s)',(id,color,precioB,precioF,stock, ))
        conexion.commit()
        cursor.close()
        conexion.close()
        print("######################!!!!!! ACABE DE AGREGAR UN PRODUCTO'!!!!!!!!!!!#################### " )
        return redirect(url_for('productos_route'))
    else:
        print("ERROR")

    return render_template('agregarProducto.html')

