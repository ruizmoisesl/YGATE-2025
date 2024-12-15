from flask import render_template, url_for, redirect, request
from deep_translator import GoogleTranslator

traductor = GoogleTranslator(source='auto', target='es')

def error_not_found(e):
    error_español= traductor.translate(str(e))
    return render_template('404.html',error = error_español)

def handle_type_error(error):
    error_e = traductor.translate(str(error))
    return "Ocurrió un error de tipo: {}".format(error), 500
