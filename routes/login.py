from flask import render_template, url_for, redirect, request, session

def login():
    return render_template('login.html')
