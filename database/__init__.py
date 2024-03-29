from pymongo import MongoClient
from .db import Database
import app_config as config

##pip install pymongo

#database = MongoClient("mongodb+srv://renancavalcanti:doDymy2pUDR4jYky@cluster0.z2hvtba.mongodb.net/?retryWrites=true&w=majority")

conn = Database(connection_string=config.CONST_MONGO_URL, database_name=config.CONST_DATABASE)
conn.connect()



