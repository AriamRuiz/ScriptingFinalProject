from flask import Blueprint, jsonify, request
import models
from database.__init__ import conn
import json
from bson.objectid import ObjectId
from controllers.user_controller import create_verb
from helpers.token_validation import validate_jwt

verb = Blueprint("verb", __name__)

#1.1
@verb.route("/verbs/", methods=["GET"])
def fetch():
    try:
        token = validate_jwt()

        if token == 400:
            return jsonify({'error': 'Token is missing in the request.'}), 400
        if token == 401:
            return jsonify({'error': 'Invalid authentication token.'}), 401

        verbs = fetch_all_verbs()

        return jsonify({'verb': verbs, 'request_made_by': token})

    except ValueError:
        return jsonify({'error': 'Error fetching verb.'}), 500

#1.2
@verb.route("/verbs/", methods=["GET"])

#1.3
@verb.route("/verbs/favorites", methods=["POST"])
def create():

    try:
        data = json.loads(request.data)
        token = validate_jwt()

        if token == 400:
            return jsonify({"error": 'Token is missing in the request, please try again'}), 401
        if token == 401:
            return jsonify({"error": 'Invalid authentication token, please login again'}), 403

        verb_created = create_verb(data)

        if verb_created == "Duplicated User":
            return jsonify({'error': 'There is already an user with this email.'}), 400

        if 'verb' not in data:
            return jsonify({"error": 'Verb is missing in the request, please try again'}), 401

    except ValueError:
        return jsonify({'verb': verb_created, 'request_made_by': token})

    except ValueError:
        return jsonify({'error': 'Error adding verb.'}), 500


@verb.route("/verbs/favorites", methods=["POST"])
def create():

    try:
        token = validate_jwt()
        if token == 400:
            return jsonify({"error": 'Token is missing in the request, please try again'}), 401
        if token == 401:
            return jsonify({"error": 'Invalid authentication token, please login again'}), 403

        data = json.loads(request.data)

        # Check for required fields
        if "verb" not in data:
            return jsonify({"error": "Verb is missing in the request"}), 422  # HTTP 422: Unprocessable Entity


        user_id = extract_user_id_from_token(token)

        # Create the new verb document
        new_verb = {
            "owner": user_id,
            "verb": data["verb"]
        }

        db.verbs.insert_one(new_verb)  # Replace with your database interaction method

        return jsonify({"message": "Verb added successfully"}), 201  # HTTP 201: Created

    except ValueError as e:
        return jsonify({"error": "Invalid request data: {}".format(str(e))}), 400  # HTTP 400: Bad Request
    except Exception as e:  # Catch any other unexpected errors
        logger.error("Error adding verb: {}".format(str(e)))  # Log the error
        return jsonify({"error": "An error occurred while adding the verb"}), 500  # HTTP 500: Internal Server Error




#1.4
@verb.route("/verbs/favourites/<favoriteUid>/", methods=["GET"])
def login():
    try:
        data = json.loads(request.data)

        if 'email' not in data:
            return jsonify({'error': 'Email is needed in the request.'}), 400
        if 'password' not in data:
            return jsonify({'error': 'Password is needed in the request.'}), 400

        login_attempt = login_user(data)

        if login_attempt == "Invalid Email":
            return jsonify({'error': 'Email not found.'}), 401
        if login_attempt == "Invalid Password":
            return jsonify({'error': 'Invalid Password.'}), 401

        return jsonify({'token': login_attempt['token'], "expiration": login_attempt['expiration'],
                        "logged_user": login_attempt["logged_user"]})
    except ValueError:
        return jsonify({'error': 'Error login user.'}), 500


#1.5
@verb.route("/verbs/favourites/", methods=["GET"])



#1.6
@verb.route("/verbs/favourites/<favoriteUid>/", methods=["DELETE"])

