from flask import Flask , render_template , Blueprint , request
from routes import index,login,register,home,information,statistics,sales,decode,productos,errors,agregarProductos
from routes.agregarProductos import agregar
from routes.editar import editarP

app = Flask(__name__)
app.register_blueprint(agregar)
app.register_blueprint(editarP)

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
    print("RUTA: productos_route")
    return productos.productos()

@app.route("/home/productos/agregarProducto", methods=['GET', 'POST'])
def agregar_producto():
    return agregarProductos.agregarProducto()

@app.route("/home/productos/editar", methods=['GET','POST'])
def editarProducto():
    numero = request.args.get('numero')
    nombre = request.args.get('nombre')
    marca = request.args.get('marca')
    referencia = request.args.get('referencia')
    color = request.args.get('color')
    precioB = request.args.get('precioB')
    precioF = request.args.get('precioF')
    stock = request.args.get('stock')
    print(numero,nombre)
    return render_template("editar.html",numero=numero,nombre=nombre,marca=marca,referencia=referencia,color=color,precioB=precioB,precioF=precioF,stock=stock)
if __name__ == "__main__":
    app.run(debug=True, port=4000)    
