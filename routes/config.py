from flask import Flask
import os

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'static/img/logos'


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'static', 'img', 'logos')