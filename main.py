import sys
from sensor.expection import SensorException
from sensor.logger import logging
from sensor.utils import dump_csv_file_to_mongodb_collection

# def test_exception() -> None:
#     try:
#         logging.info("Ekhane ekta error eseche, zero diye divide hoy na! ")
#         a = 1/0
#     except Exception as e:
#         raise SensorException(e, sys)


if __name__ == "__main__":
    filepath = "/home/ryle/Desktop/SensorLive/aps_failure_training_set1.csv"
    database_name = "live_sensor_project"
    collection_name = "sensors"
    
    dump_csv_file_to_mongodb_collection(filepath, database_name, collection_name)