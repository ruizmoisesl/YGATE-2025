from flask import render_template, url_for, redirect, request

def error_not_found(e):
    return render_template('404.html',error = e)