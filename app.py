from flask import Flask
from routes import index,login,register,home,information, statistics, sales,productos,errors,agregarProductos
import os
from dotenv import load_dotenv

load_dotenv()


app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

UPLOAD_FOLDER = os.path.join(BASE_DIR, 'static', 'img', 'logos')

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def index_route():
    return index.index()

@app.route('/login', methods=['GET', 'POST'])
def login_route():
    return login.login()

@app.route('/register', methods=['GET', 'POST'])
def register_route():
    return register.register()

@app.route('/home')
def home_route():
    return home.home()

@app.route('/home/profile')
def information_route():
    return information.information()

@app.route('/home/statistics')
def statistics_route():
    
    return  statistics.statistics()

@app.route('/home/sales')
def sales_route():
    return sales.sales()


@app.errorhandler(404)
def page_not_found(e):
    return errors.error_not_found(e)


@app.route("/home/productos")
def productos_route():
    return productos.productos()

@app.route("/home/productos/agregarProducto", methods=['GET', 'POST'])
def agregar_producto():
    return agregarProductos.agregarProducto()


if __name__ == "__main__":
    app.run(debug=True, port=4000)    
