from flask import render_template, url_for, redirect, request, session

def register():
    return render_template('register.html')