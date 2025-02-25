from flask import render_template, url_for, redirect, request, session

def information():
    datos_tienda = session.get('datos_tienda')
    return render_template('information.html', tienda= datos_tienda)