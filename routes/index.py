from flask import render_template, url_for, redirect, request

def index():
    return render_template('index.html')