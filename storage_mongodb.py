from pymongo import MongoClient
from pymongo.server_api import ServerApi

import config_mongo
from models import Currency, NBUCurrency


class MongoStorage:
    def __init__(self):
        mongo_url = config_mongo.MONGO_CONNECTION_STRING.format(
            user=config_mongo.MONGO_USER,
            password=config_mongo.MONGO_PASSWORD,
        )

        client = MongoClient(
            mongo_url,
            server_api=ServerApi('1'),
            tlsAllowInvalidCertificates=True
        )
        db = client["mydatabase"]
        self.collection = db["currencies"]
        self.nbu_collection = db['data_nbu']

    def add_currency(self, currency: Currency):
        self.collection.insert_one(currency.model_dump())

    def add_nbu_currency(self, currency: NBUCurrency):
        self.nbu_collection.insert_one(currency.model_dump())


storage = MongoStorage()
