from flask import Flask, jsonify
from flask_cors import CORS
from prometheus_client import generate_latest, Gauge

# setup flask app
app = Flask(__name__)
CORS(app)

# register a prometheus gauge
api_counter = Gauge('api_counter', 'API hits')

# api endpoints
@app.route("/increment")
def inc():
    api_counter.inc()
    return jsonify({'value': api_counter._value.get()})

@app.route("/decrement")
def dec():
    api_counter.dec()
    return jsonify({'value': api_counter._value.get()})

@app.route("/value")
def value():
    return jsonify({'value': api_counter._value.get()})

@app.route("/metrics")
def metrics():
    return generate_latest()

@app.route("/")
def index():
    return open('index.html').read()

# run app on port 9001
if __name__ == '__main__':
    app.run('localhost', 9001)