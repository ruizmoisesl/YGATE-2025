from flask import render_template, url_for, redirect, request, session,flash
import bcrypt
from database import iniciar_connection

def login():
    nit = 0

    if request.method == 'POST':
        email = request.form['email']
        contraseña = request.form['contraseña']

        mysql = iniciar_connection()
        cursor = mysql.cursor()

        cursor.execute('SELECT * FROM tienda WHERE gmail = %s ', (email,))
        tienda = cursor.fetchone()
        cursor.close()
        mysql.close()

        if tienda is None:
            flash('Usuario no encontrado')
            return redirect(url_for('login_route'))
        
        session['datos_tienda'] = tienda
        session['nit'] = tienda[0]
        contraseña_db = tienda[5].encode()      
        if bcrypt.checkpw(contraseña.encode(), contraseña_db):
            print(nit,"313#!#!#!#!#!##!#!#!#!")
            return redirect(url_for('productos.productos'))

        else:
            flash('Contraseña incorrecta. Intenta de nuevo')
            return redirect(url_for('login_route'))

        
    return render_template('login.html') 
