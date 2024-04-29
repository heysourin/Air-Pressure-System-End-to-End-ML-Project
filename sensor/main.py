import sys
from sensor.expection import SensorException


def test_exception() -> None:
    try:
        a = 1/0
    except Exception as e:
        raise SensorException(e, sys)


if __name__ == "__main__":
    try:
        test_exception()
    except Exception as e:
        print("Error: " + str(e))
