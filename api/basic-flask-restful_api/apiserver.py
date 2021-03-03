#!/usr/bin/env python
"""
Car Store App
"""
import argparse
import os
import json
import requests
import logging
from flask import Flask, request, jsonify, make_response, abort, url_for

__version__ = "0.0.1"

app = Flask(__name__, static_url_path=None, static_folder=None)

cars = {}
status = {}

# ===============================================
# Python Script arguments and
# environment variables declaration
# ===============================================
parser = argparse.ArgumentParser()
parser.parse_known_args()
parser.add_argument('-f', '--filename', help='Specifies the path to the dataset JSON file to serve.', default=os.environ.get('CARS_INVENTORY_FILE', None))
parser.add_argument('-s', '--status-filename', help='Specifies the path to the dataset JSON file to serve.', default=os.environ.get('CARS_STATUS_FILE', None))
parser.add_argument('-u', '--opa-url', help='Specifies the OPA proxy server URL.', default=os.environ.get('OPA_URL', 'http://localhost:8181'))
# Logger arguments
parser.add_argument('-d', '--debug', help="Enable debug logging", action="store_true")
args = parser.parse_args()

# ===============================================
# Logging configuration
# ===============================================
def setup_logging():
    if args.debug:
        for handler in app.logger.handlers:
            handler.setLevel(logging.DEBUG)
        app.logger.setLevel(logging.DEBUG)
    else:
        for handler in app.logger.handlers:
            handler.setLevel(logging.INFO)
        app.logger.setLevel(logging.INFO)

# ===============================================
# Routes
# ===============================================
@app.route("/", methods=["GET"])
def list_routes():
    import urllib
    routes = set([])
    for rule in app.url_map.iter_rules():
        options = {}
        for arg in rule.arguments:
            options[arg] = '[{0}]'.format(arg)
        url = urllib.parse.unquote(url_for(rule.endpoint, **options))
        routes.add(url)
    return jsonify(sorted(routes))

@app.route("/cars", methods=["GET"])
def list_cars():
    result = []
    for id in cars:
        result.append(cars[id])
    return jsonify({'result': result})

@app.route("/cars/<id>", methods=["GET"])
def car_detail(id):
    if id not in cars:
        abort(404)
    return jsonify({'result': cars[id]})

@app.route("/cars/<id>", methods=["PUT"])
def car_update(id):
    cars[id] = request.json
    return jsonify({'result': cars[id]})

@app.route("/cars/<id>", methods=["DELETE"])
def delete_car(id):
    if id not in cars:
        abort(404)
    car = cars[id]
    del cars[id]
    return jsonify({'result': car})

@app.route("/cars/<id>/status", methods=["GET"])
def car_status_detail(id):
    if id not in status:
        abort(404)
    return jsonify({'result': status[id]})

@app.route("/cars/<id>/status", methods=["PUT"])
def add_car_status(id):
    status[id] = request.json
    return jsonify({'result': status[id]})

# ===============================================
# AuthZ
# ===============================================
@app.before_request
def check_authorization():
    try:
        input_request = json.dumps({
                        "method": request.method,
                        "path": request.path.strip().split("/")[1:],
                        "user": get_authentication(request),
        }, indent=2)
        url = args.opa_url
        app.logger.debug("OPA query: %s. Body: %s", url, input_request)
        response = requests.post(url, data=input_request)
    except Exception as e:
        app.logger.exception("Unexpected error querying OPA.")
        abort(500)

    if response.status_code != 200:
        app.logger.error("OPA status code: %s. Body: %s",
                         response.status_code, response.json())
        abort(500)

    allowed = response.json()
    app.logger.debug("OPA result: %s", allowed)
    if not allowed:
        abort(403)

def get_authentication(request):
    return request.headers.get("Authorization", "")

def pump_db():
    # Read inventory
    with open(args.filename) as json_file:
        mock_cars = json.load(json_file)
        for car in mock_cars['items']:
            cars[car["id"]] = car

    # Read status
    with open(args.status_filename) as json_file:
        mock_status = json.load(json_file)
        for s in mock_status['items']:
            status[s["id"]] = s

if __name__ == "__main__":
    setup_logging()
    pump_db()
    app.run(host="0.0.0.0", port="8080")