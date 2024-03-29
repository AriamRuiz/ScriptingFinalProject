from flask import Blueprint, jsonify, request
from database.__init__ import conn
import json
from bson.objectid import ObjectId
from controllers.verb_controller import add_verb
from helpers.token_validation import validate_jwt

verb = Blueprint("verb", __name__)

@verb.route("/verbs/favorites", methods=["POST"])
def add_favorite():
    try:
        token = validate_jwt()

        if token == 400:
            return jsonify({"error": 'Token is missing in the request, please try again'}), 401
        if token == 401:
            return jsonify({"error": 'Invalid authentication token, please login again'}), 403

        data = json.loads(request.data)

        if 'verb' not in data:
            return jsonify({'error': 'verb is needed in the request.'}), 400

        added_verb = add_verb(data['verb'], token['id'])

        if added_verb == "Duplicated Verb":
            return jsonify({'error': 'The user already added this verb.'}), 400

        return jsonify({'user id': token['id']})
        ##return jsonify({'id': added_verb['owner'], 'verb' : added_verb['verb']})

    except ValueError:
        return jsonify({'error': 'Error fetching users.'}), 500