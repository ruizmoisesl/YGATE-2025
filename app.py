from flask import Flask , render_template
from routes import index,login,register,home,information, statistics, sales,decode,productos,errors

app = Flask(__name__)

@app.route('/')
def index_route():
    return index.index()

@app.route('/login')
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

@app.route('/decode', methods=['GET', 'POST'])
def decode_route(code):
    if code:   
        return decode.decode(code)
    else:
        return decode.decode(code = '6928804011128')

@app.errorhandler(404)
def page_not_found(e):
    return errors.error_not_found(e)


@app.route("/home/productos")
def productos_route():
    return productos.productos()

if __name__ == "__main__":
    app.run(debug=True, port=4000)