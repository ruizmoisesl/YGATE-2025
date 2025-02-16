from flask import render_template, url_for, redirect, request, session
import os
from routes.config import UPLOAD_FOLDER


def register():
    if request.method == 'POST':
        nombre_empresa = request.form['nombre']
        email = request.form['email']
        telefono = request.form['telefono']
        nit = request.form['nit']
        contraseña = request.form['contraseña']
        repetir_contraseña = request.form['repetir-contraseña']
        file = request.files['logo']

        if file and file.filename.lower().endswith(('png', 'jpg', 'jpeg', 'gif')):
            file_path = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(file_path)
        
        return redirect(url_for('register_route'))

    print("La carpeta de subida está en:", UPLOAD_FOLDER)
    return render_template('register.html')