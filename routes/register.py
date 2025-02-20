from flask import render_template, url_for, redirect, request, session,jsonify
import cloudinary
import cloudinary.api
import cloudinary.uploader
import routes.config 


def register():
    if request.method == 'POST':
        nombre_empresa = request.form['nombre']
        email = request.form['email']
        telefono = request.form['telefono']
        nit = request.form['nit']
        contraseña = request.form['contraseña']
        repetir_contraseña = request.form['repetir-contraseña']
        file = request.files['logo']


        result = cloudinary.uploader.upload(
            file,
            folder="logos",
            public_id=file.filename.split('.')[0],
            resource_type="image"
        )

        secure_url = result.get("secure_url")

    return render_template('register.html')