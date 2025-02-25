from flask import render_template, url_for, redirect, request, session

def home():
    datos_tienda = session.get('datos_tienda')
    return render_template('home.html', tienda = datos_tienda)