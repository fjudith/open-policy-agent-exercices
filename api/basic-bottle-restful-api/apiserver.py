#!/usr/bin/env python
"""
Car Store App
"""
import argparse
import os
import json
import requests
import logging
from bottle import Bottle, run, abort, request, response, get , put, delete, hook, route

# Remove "hop-by-hop" headers (as defined by RFC2613, Section 13)
# since they are not allowed by the WSGI standard.
FILTER_HEADERS = [
    'Connection',
    'Keep-Alive',
    'Proxy-Authenticate',
    'Proxy-Authorization',
    'TE',
    'Trailers',
    'Transfer-Encoding',
    'Upgrade',
]

PROJECT_DIR = os.path.dirname(__file__)
WEB_ROOT = os.path.join(PROJECT_DIR, "snap-audit", "build")
STATIC_ROOT = os.path.join(WEB_ROOT, "static")

__verison__ = "0.0.1"

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
logger = logging.getLogger('Car Store App')
ch = logging.StreamHandler()
if args.debug:
    logger.setLevel(logging.DEBUG)
    ch.setLevel(logging.DEBUG)
else:
    logger.setLevel(logging.INFO)
    ch.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

# ===============================================
# Routes
# ===============================================
@get('/')
def list_routes():
    routes = [
        "/",
        "/cars",
        "/cars/[id]",
        "/cars/[id]/status"
    ]
    return dict({'result': routes})

@get('/cars')
def list_cars():
    result = []
    for id in cars:
        result.append(cars[id])
    return dict({'result': result})

@get('/cars/<id>')
def car_detail(id):
    if id not in cars:
        abort(404)
    response.content_type = 'application/json'
    return dict({'result': cars[id]})

@put('/car/<id>')
def car_update(id):
    cars[id] = request.json
    response.content_type = 'application/json'
    return dict({'result': cars[id]})

@delete('/cars/<id>')
def delete_car(id):
    if id not in cars:
        abort(404)
    car = cars[id]
    del cars[id]
    response.content_type = 'application/json'
    return dict({'result': car})

@get('/cars/<id>/status')
def car_status_detail(id):
    if id not in status:
        abort(404)
    response.content_type = 'application/json'
    return dict({'result': status[id]})

@put('/cars/<id>/status')
def add_car_status(id):
    status[id] = request.json
    response.content_type = 'application/json'
    return dict({'result': status[id]})

# ===============================================
# AuthZ
# ===============================================
@hook("before_request")
def check_authorization():
    try:
        input_request = json.dumps({
                        "method": request.method,
                        "path": request.path.strip().split("/")[1:],
                        "user": get_authentication(request),
        }, indent=2)
        url = args.opa_url
        logger.debug("OPA query: %s. Body: %s", url, input_request)
        request_response = requests.post(url, data=input_request)
    except Exception as e:
        logger.exception("Unexpected error querying OPA.")
        abort(500)

    if request_response.status_code != 200:
        logger.error("OPA status code: %s. Body: %s",
                      request_response.status_code, 
                      request_response.json())
        abort(500)

    allowed = request_response.json()
    logger.debug("OPA result: %s", allowed)
    if not allowed:
        abort(403)

def get_authentication(request):
    return request.headers.get("Authorization", "")

def pump_db():
    # Read inventory
    logger.debug("Importing inventory file: %s.", args.filename)
    with open(args.filename) as json_file:
        mock_cars = json.load(json_file)
        for car in mock_cars['items']:
            cars[car["id"]] = car

    # Read status
    logger.debug("Importing status file: %s.", args.filename)
    with open(args.status_filename) as json_file:
        mock_status = json.load(json_file)
        for s in mock_status['items']:
            status[s["id"]] = s

if __name__ == '__main__':
    pump_db()
    run(host = '0.0.0.0', port = 8080)