
# https://github.com/kasbert/epsolar-tracer
from pyepsolartracer.client import EPsolarTracerClient
from flask import Flask, jsonify, current_app
from regs import registers as regs
from waitress import serve
from flask_cors import CORS, cross_origin

import logging

app = Flask(__name__)

app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy Matt'
app.config['CORS_HEADERS'] = 'Content-Type'

cors = CORS(app, resources={r"/": {"origins": "http://localhost:5000"}})


def get_charger_data(registers):
    client = EPsolarTracerClient(serialclient=None)
    client.connect()
    output = dict()
    for key in registers.iterkeys():
        value = client.read_input(key)
        output[key] = {'name': value.register.name, 'description': value.register.description, 'value': value.value}
    client.close()
    return output


@app.route('/')
@cross_origin(origin='localhost', headers=['Content-Type', 'Authorization'])
def default():
    return current_app.send_static_file('json.html')


@app.route('/json')
@cross_origin(origin='localhost', headers=['Content-Type', 'Authorization'])
def json_data():
    return jsonify(get_charger_data(regs))


if __name__ == '__main__':
    logging.basicConfig()
    log = logging.getLogger()
    log.setLevel(logging.INFO)
    serve(app, listen='0.0.0.0:5000', threads=1)
