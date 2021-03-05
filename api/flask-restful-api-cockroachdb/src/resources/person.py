"""
Define the REST verbs relative to the persons
"""

from flasgger import swag_from
from flask.json import jsonify
from flask_restful import Resource
from flask_restful.reqparse import Argument

from repositories import PersonRepository
from util import parse_params


class PersonResource(Resource):
    """ Verbs relative to the persons """

    @staticmethod
    @swag_from("../swagger/person/GET.yaml")
    def get(guid):
        """ Return an person key information base on his name """
        person = PersonRepository.get(guid=guid)
        return jsonify({"person": person.json})
    
    @staticmethod
    @parse_params(
        Argument("age", location="json", required=True, help="The age of the person.")
    )
    @swag_from("../swagger/person/POST.yaml")
    def post(guid, age):
        """ Create a person based on the sent information """
        person = PersonRepository.create(
            guid=guid, age=age
        )
        return jsonify({"person": person.json})

    @staticmethod
    @parse_params(
        Argument("age", location="json", required=True, help="The age of the person.")
    )
    @swag_from("../swagger/person/PUT.yaml")
    def put(guid, age):
        """ Update a person based on the sent information """
        repository = PersonRepository()
        person = repository.update(guid=guid, age=age)
        return jsonify({"person": person.json})
