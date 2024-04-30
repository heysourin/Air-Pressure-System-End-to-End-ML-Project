import sys
from sensor.expection import SensorException
from sensor.logger import logging


def test_exception() -> None:
    try:
        logging.info("Ekhane ekta error eseche, zero diye divide hoy na!")
        a = 1/0
    except Exception as e:
        raise SensorException(e, sys)


if __name__ == "__main__":
    try:
        test_exception()
    except Exception as e:
        print("Error: " + str(e))
