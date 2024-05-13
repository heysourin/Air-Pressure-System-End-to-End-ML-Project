import os
import sys
import pymongo
from sklearn.model_selection import train_test_split
from sensor.expection import SensorException
from sensor.logger import logging
import pandas as pd
from pandas import DataFrame  # DataFrame
from sensor.entity.config_entity import DataIngestionConfig  # artifact file path
from sensor.entity.artifact_entity import DataIngestionArtifact
from sensor.data_access.sensor_data import SensorData  # to upload and download data
from sensor.utils.main_utils import read_yaml_file
from sensor.constant.training_pipeline import SCHEMA_FILE_PATH
from sensor.constant.env_variable import MONGODB_URL_KEY
from sensor.constant.database import DATABASE_NAME, COLLECTION_NAME


class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig):
        try:
            self.data_ingestion_config = data_ingestion_config
            self._schema_config = read_yaml_file(SCHEMA_FILE_PATH)

        except Exception as e:
            raise SensorException(e, sys)

    def export_data_into_feature_store(self, database_name, collection_name) -> DataFrame:
        """
        Export mongo db collection record as data frame into feature folder
        """
        try:
            logging.info("Exporting data from mongodb to feature store")

            sensor_data = SensorData()

            self.dataframe = sensor_data.export_collection_as_dataframe(
                database_name, collection_name)

            feature_store_file_path = self.data_ingestion_config.feature_store_file_path

            # creating folder

            dir_path = os.path.dirname(feature_store_file_path)
            os.makedirs(dir_path, exist_ok=True)

            self.dataframe.to_csv(feature_store_file_path,
                                  index=False, header=True)

            logging.info("Dataframe return successfull: data_ingestion.py")
            return self.dataframe
        except Exception as e:
            raise SensorException(e, sys)

    def split_data_as_train_test(self, dataframe: DataFrame) -> None:
        try:
            if dataframe.empty:
                logging.error(
                    "Dataframe is empty. Cannot perform train-test split.")
                return

            train_set, test_set = train_test_split(
                dataframe, test_size=self.data_ingestion_config.train_test_split_ratio)

            logging.info(
                "Performed split_data_as_train_test of DataIngestion class")

            logging.info(
                "Exited split_data_as_train_test method of Data_Ingestion class")

            dir_path = os.path.dirname(
                self.data_ingestion_config.training_file_path)

            os.makedirs(dir_path, exist_ok=True)

            logging.info(f"Exporting train and test file path")

            train_set.to_csv(
                self.data_ingestion_config.training_file_path, index=False, header=True)

            test_set.to_csv(
                self.data_ingestion_config.testing_file_path, index=False, header=True)

            logging.info(f"Exporting train and test set as CSV files to respective folders")

        except Exception as e:
            raise SensorException(e, sys)

    def initiate_data_ingestion(self) -> DataIngestionArtifact:
        try:

            dataframe = self.export_data_into_feature_store(
                DATABASE_NAME, COLLECTION_NAME) 

            columns_to_drop = [
                col for col in self._schema_config["drop_columns"] if col in dataframe.columns]
            dataframe = dataframe.drop(columns_to_drop, axis=1)

            # dataframe = dataframe.drop(
            # self._schema_config["drop_columns"], axis=1)

            self.split_data_as_train_test(dataframe=dataframe)

            data_ingestion_artifact = DataIngestionArtifact(
                trained_file_path=self.data_ingestion_config.training_file_path, test_file_path=self.data_ingestion_config.testing_file_path)
            logging.info(f"data ingestion ln6")

            return data_ingestion_artifact
        except Exception as e:
            raise Exception(e, sys)
