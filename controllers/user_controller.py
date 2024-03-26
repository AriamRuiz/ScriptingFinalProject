from database.__init__ import conn
import app_config as config
import bcrypt
from datetime import datetime, timedelta
import jwt
from models.verbs_model import Regular_Verb


def generate_hash_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode("utf-8"), salt)
    return hashed_password


def create_verb(user_information):
    try:
        new_verb = Regular_Verb(user_information["verb"])
        new_verb.verb = user_information["verb"]

        db_collection = conn.database[config.CONST_USER_COLLECTION]

        if db_collection.find_one({'verb': new_verb.verb}):
            return 'Duplicated Verb'

        created_verb = db_collection.insert_one(new_verb.__dict__)

        return created_verb
    except Exception as err:
        raise ValueError("Error on adding the new Verb.", err)


def login_user(user_information):
    try:
        email = user_information["email"]
        password = user_information["password"].encode('utf-8')

        db_collection = conn.database[config.CONST_USER_COLLECTION]

        current_user = db_collection.find_one({'email': email})

        if not current_user:
            return "Invalid Email"

        if not bcrypt.checkpw(password, current_user["password"]):
            return "Invalid Password"

        logged_user = {}
        logged_user['id'] = str(current_user['_id'])
        logged_user['email'] = current_user['email']
        logged_user['name'] = current_user['name']

        expiration = datetime.utcnow() + timedelta(seconds=config.JWT_EXPIRATION)

        jwt_data = {'email': logged_user['email'], 'id': logged_user['id'], 'exp': expiration}

        jwt_to_return = jwt.encode(payload=jwt_data, key=config.TOKEN_SECRET)

        # print(jwt_to_return)

        return {'token': jwt_to_return, 'expiration': config.JWT_EXPIRATION, 'logged_user': logged_user}

    except Exception as err:
        raise ValueError("Error on trying to login.", err)


def fetch_all_users():
    try:
        db_collection = conn.database[config.CONST_USER_COLLECTION]
        users = []

        for user in db_collection.find():
            current_user = {}
            current_user["id"] = str(user["_id"])
            current_user["email"] = user["email"]
            current_user["name"] = user["name"]
            users.append(current_user)

        return users

    except Exception as err:
        raise ValueError("Error on trying to fetch users.", err)