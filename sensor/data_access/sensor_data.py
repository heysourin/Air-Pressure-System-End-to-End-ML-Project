import sys
from typing import Optional

import numpy as np
import pandas as pd
import json
from sensor.configuration.mongo_db_connection import MongoDBClient
from sensor.constant.database import DATABASE_NAME
from sensor.expection import SensorException
from sensor.logger import logging


class SensorData:
    """
    This class helps to export entrire mongodb record as pandas dataframe
    """

    def __init__(self):
        try:
            # self.mongo_client = MongoDBClient(database_name=DATABASE_NAME)
            self.mongo_client = MongoDBClient()
        except Exception as e:
            raise SensorException(e, sys)

    def save_csv_file(self, file_path, collection_name: str, database_name: Optional[str] = None):
        """
        Uploads the data to mongodb
        """
        try:
            data_frame = pd.read_csv(file_path)
            data_frame.reset_index(drop=True, inplace=True)
            records = list(json.loads(data_frame.T.to_json()).values())

            # if database_name is None:
            #     collection = self.mongo_client.database[collection_name]
            # else:
            #     collection = self.mongo_client.client[database_name][collection_name]

            db = self.mongo_client.client[database_name]
            collection = db[collection_name]
            collection.insert_many(records)

            return len(records)

        except Exception as e:
            raise SensorException(e, sys)

    def export_collection_as_dataframe(self, database_name: str, collection_name: str) -> pd.DataFrame:
        try:
            logging.info(
                "Downloading from Mongodb collection and returning datafram for exporting to artifacts")
            self.db = self.mongo_client.client[database_name]
            self.collection = self.db[collection_name]

            self.dataframe = pd.DataFrame(list(self.collection.find()))

            if "_id" in self.dataframe.columns.tolist():
                self.dataframe = self.dataframe.drop(columns=["_id"], axis=1)

            self.dataframe.replace({"na": np.nan}, inplace=True)

            return self.dataframe
        except Exception as e:
            raise SensorException(e, sys)
