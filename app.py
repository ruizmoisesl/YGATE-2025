from flask import Flask , render_template , Blueprint
from routes import index,login,register,home,information, statistics, sales,decode,productos,errors,agregarProductos
from routes.agregarProductos import agregar

app = Flask(__name__)
app.register_blueprint(agregar, url_prefix='/agregar')

@app.route('/')
def index_route():
    return index.index()

@app.route('/login', methods=['GET', 'POST'])
def login_route():
    return login.login()

@app.route('/register')
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
    print("RUTA: productos_route")
    return productos.productos()

@app.route("/home/productos/agregarProducto", methods=['GET', 'POST'])
def agregar_producto():
    return render_template("agregarProducto.html"),agregarProductos.agregarProducto()

if __name__ == "__main__":
    app.run(debug=True, port=4000)