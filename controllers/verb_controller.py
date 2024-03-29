from models.verb_model import Verb
from database.__init__ import conn
import app_config as config
import bcrypt
from datetime import datetime, timedelta
import jwt

def add_verb(verb_info, verb_owner):
    try:
        new_verb = Verb()
        new_verb.owner = verb_owner
        new_verb.verb = verb_info

        db_collection = conn.database[config.CONST_VERB_COLLECTION]

        if db_collection.find_one({'owner':new_verb.owner,'verb': new_verb.verb}):
            return 'Duplicated Verb'

        added_verb = db_collection.insert_one(new_verb.__dict__)

        return added_verb
    except Exception as err:
        raise ValueError("Error on adding favorite verb.", err)