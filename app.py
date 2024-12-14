from flask import Flask
from routes import home,information, statistics, sales,errors

app = Flask(__name__)

@app.route('/home')
def home_route():
    return home.home()

@app.route('/profile')
def information_route():
    return information.information()

@app.route('/statistics')
def statistics_route():
    return  statistics.statistics()

@app.route('/sales')
def sales_route():
    return sales.sales()

@app.errorhandler(404)
def page_not_found(e):
    return errors.error_not_found(e)

if __name__ == "__main__":
    app.run(debug=True, port=4000)