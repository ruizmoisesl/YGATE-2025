from flask import Flask, session, request, redirect, url_for, render_template , Blueprint
import secrets
import os
import base64
import bcrypt
from werkzeug.utils import secure_filename
import mysql.connector as MySQLdb
from database import iniciar_connection


app = Flask(__name__)
borrar = Blueprint('borrar', __name__)
mysql = None

@borrar.route("/borrarProducto", methods=['GET', 'POST'])
def borrarPro():
    conexion = iniciar_connection()
    cursor = conexion.cursor()
    numero = request.args.get('numero')
    cursor.execute('DELETE FROM Productos WHERE ID_Producto = %s',(numero,))
    cursor.execute('DELETE FROM Detalles_Producto WHERE ID_Producto = %s',(numero,))
    conexion.commit()
    cursor.close()
    conexion.close()
    return redirect(url_for('productos_route'))
