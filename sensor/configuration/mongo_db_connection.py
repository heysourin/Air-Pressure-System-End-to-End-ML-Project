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

            logging.info(f"MongoDB URL Retrieved: %s" % mongo_db_url)

        except Exception as e:
            raise SensorException(e, sys)

# class MongoDBClient:

#     def __init__(self, database_name: DATABASE_NAME) -> None:
#         try:
#             mongo_db_url = os.getenv(MONGODB_URL_KEY)
#             logging.info(f"Retrieved MongoDB URL: {mongo_db_url}")

#             if "localhost" in mongo_db_url:
#                 self.client = pymongo.MongoClient(mongo_db_url)
#             else:
#                 self.client = pymongo.MongoClient(
#                     mongo_db_url, tlsCAFile=ca)  # tls/ssl

#             self.database = self.client[database_name]
#             self.database_name = database_name

#             logging.info(f"DB connected successfully, DB name: {self.database_name}")
#         except Exception as e:
#             logging.error(f"Error initializing MongoDB client: {e}")
#             raise


# class MongoDBClient:
#     client = None

#     def __init__(self, database_name: DATABASE_NAME) -> None:
#         try:
#             if MongoDBClient.client is None:
#                 mongo_db_url = os.getenv(MONGODB_URL_KEY)
#                 logging.info(f"Retrived MongoDB URL: {mongo_db_url}")

#                 if "localhost" in mongo_db_url:
#                     MongoDBClient.client = pymongo.MongoClient(mongo_db_url)
#                 else:
#                     MongoDBClient.client = pymongo.MongoClient(
#                         mongo_db_url, tlsCAFile=ca)  # tls/ssl

#             self.client = MongoDBClient.client
#             self.database = self.client[database_name]
#             self.database_name = database_name

#         except Exception as e:
#             logging.error(f"Error initializing MongoDB client: {e}")
#             raise
