from flask import render_template, url_for, redirect, request

def decode(code):
    information = code
    return render_template('scaner.html', information = information)