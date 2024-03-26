from pymongo import MongoClient
from .db import Database
import app_config as config

conn = Database(connection_string=config.CONST_MONGO_URl, database_name=config.CONST_DATABASE)
conn.connect()
