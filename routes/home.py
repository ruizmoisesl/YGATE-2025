from flask import render_template, url_for, redirect, request

def home():
    return render_template('home.html')