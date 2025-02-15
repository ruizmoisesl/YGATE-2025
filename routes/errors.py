from flask import render_template, url_for, redirect, request
from deep_translator import GoogleTranslator
def error_not_found(e):
    error = e
    error_traducido = GoogleTranslator(source='auto', target='es').translate(error)
    return render_template("404.html",error= error_traducido), 404

