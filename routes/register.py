from flask import render_template, url_for, redirect, request, session,jsonify,flash
import cloudinary
import cloudinary.api
import cloudinary.uploader
import bcrypt
import routes.config
from database import iniciar_connection


def register():
    if request.method == 'POST':
        nombre_empresa = request.form['nombre']
        email = request.form['email']
        telefono = request.form['telefono']
        nit = request.form['nit']
        contraseña = request.form['contraseña']
        repetir_contraseña = request.form['repetir-contraseña']
        file = request.files['logo']

        if contraseña == repetir_contraseña:
            
            mysql= iniciar_connection()
            cursor= mysql.cursor()

            hashed = bcrypt.hashpw(contraseña.encode(), bcrypt.gensalt())

            result = cloudinary.uploader.upload(
                file,
                folder="logos",
                public_id=file.filename.split('.')[0],
                resource_type="image"
            )
            secure_url = result.get("secure_url")

            cursor.execute('INSERT INTO tienda (nit,nombreEmpresa,gmail, telefono, url_imagen, contraseña) VALUES (%s,%s,%s,%s,%s,%s)', (nit,nombre_empresa,email,telefono, secure_url, hashed))
            
            mysql.commit()
            cursor.close()
            mysql.close()

            flash('Registro realizado con exito. Inicia sesion')
            return redirect(url_for('login_route'))

    return render_template('register.html')