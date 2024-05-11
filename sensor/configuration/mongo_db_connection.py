from dotenv import load_dotenv
from sensor.constant.database import DATABASE_NAME, COLLECTION_NAME
from sensor.constant.env_variable import MONGODB_URL_KEY
from sensor.expection import SensorException
import pymongo
import os
import sys
import logging
import certifi
ca = certifi.where()

load_dotenv()


class MongoDBClient:
    def __init__(self) -> None:
        try:
            mongo_db_url = os.getenv(MONGODB_URL_KEY)
            self.client = pymongo.MongoClient(mongo_db_url)

            logging.info(f"MongoDB URL Retrieved:{mongo_db_url} and connection established")

        except Exception as e:
            raise SensorException(e, sys)