from flask import render_template, url_for, redirect, request


def productos():
     return render_template("productos.html")