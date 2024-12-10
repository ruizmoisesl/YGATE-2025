from flask import Flask
from routes import index,information, statistics

app = Flask(__name__)

@app.route('/information')
def information_route():
    return information.information()

@app.route('/statistics')
def statistics_route():
    return  statistics.statistics()


if __name__ == "__main__":
    app.run(debug=True)