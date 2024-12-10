from flask import render_template, url_for, redirect, request
from deep_translator import GoogleTranslator

traductor = GoogleTranslator(source='auto', target='es')

def error_not_found(e):
    error_español= traductor.translate(str(e))
    return render_template('404.html',error = error_español)