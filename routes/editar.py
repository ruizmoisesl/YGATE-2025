from flask import Flask, session, request, redirect, url_for, render_template , Blueprint
import secrets
import os
import base64
import bcrypt
from werkzeug.utils import secure_filename
import mysql.connector as MySQLdb

app = Flask(__name__)
editarP = Blueprint('editarP', __name__)
mysql = None

@editarP.route("/editarProducto", methods=['GET', 'POST'])
def editarPro():
    try:
        mysql = MySQLdb.connect(
        host="bogk9mha8ehn5owk1qeo-mysql.services.clever-cloud.com",
        user="udq78qvouupy05hi",
        passwd="FjhgEsSoU9KepA4XgIxR",
        db="bogk9mha8ehn5owk1qeo"
    )
    
    except MySQLdb.Error as e:
        print(f"Error al conectar: {e}")
    if request.method == 'POST':
        nombre = request.form['nombre']
        marca = request.form['marca']
        referencia = request.form['referencia']
        color = request.form['color']
        precioB = request.form['precioB']
        precioF = request.form['precioF']
        stock = request.form['stock']
        numero = request.form['id']
        print(nombre,marca,referencia,color,precioB,precioF,stock,numero,"editar")
        cursor = mysql.cursor()
        cursor.execute('UPDATE Productos SET Nombre=%s,Marca=%s,Referencia=%s WHERE ID_Producto = %s',(nombre,marca,referencia,numero))
        cursor.execute('UPDATE Detalles_Producto SET Color=%s,Precio_Base=%s,Precio_Final=%s,Stock=%s WHERE ID_Producto = %s',(color,precioB,precioF,stock,numero))
        mysql.commit()
        cursor.close()
        return redirect(url_for('productos_route'))
    else:
        print("ERROR")

    return render_template('agregarProducto.html')
