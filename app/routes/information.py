from flask import render_template, url_for, redirect, request

def information():
    return render_template('information.html')