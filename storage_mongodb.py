import datetime
from datetime import date

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
        self.currencies_collection = db["currencies"]
        self.nbu_collection = db['data_nbu']

    def add_currency(self, currency: Currency):
        self.currencies_collection.insert_one(currency.model_dump())

    def add_nbu_currency(self, currency: NBUCurrency):
        self.nbu_collection.insert_one(currency.model_dump())

    def get_user_info(self, short_name_currency: str, exchange_date: date):
        from_date = datetime.datetime.combine(exchange_date, datetime.time.min)
        to_date = datetime.datetime.combine(exchange_date + datetime.timedelta(days=1), datetime.time.min)
        result = list(self.currencies_collection.find({
            'short_name_currency': short_name_currency,
            'exchange_date': {"$gte": from_date, "$lt": to_date}
        }))
        return [Currency(**r) for r in result]

    def get_nbu_info(self, short_name_currency: str, exchange_date: date):
        from_date = datetime.datetime.combine(exchange_date, datetime.time.min)
        to_date = datetime.datetime.combine(exchange_date + datetime.timedelta(days=1), datetime.time.min)
        result = list(self.nbu_collection.find({
            'short_name_currency': short_name_currency,
            'exchange_date': {"$gte": from_date, "$lt": to_date}
        }))
        result = [NBUCurrency(**r) for r in result]
        if result:
            return result[0]
        else:
            return None


storage = MongoStorage()
