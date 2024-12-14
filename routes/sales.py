from flask import render_template, url_for, redirect, request

def sales():
    return render_template('sales.html')