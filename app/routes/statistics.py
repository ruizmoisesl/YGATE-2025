from flask import render_template, url_for, redirect, request

def statistics():
    return render_template('statistics.html')