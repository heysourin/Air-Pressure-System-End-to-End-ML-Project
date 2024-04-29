import sys
import os


def error_message_details(error, error_details: sys):
    # _, _, exc_tb = sys.exc_error_detail.exc_info()
    # return f"Exception Type: {exc_type}, Exception Value: {exc_value}, Line Number: {exc_tb.tb_lineno}"
    _, _, exc_tb = sys.exc_info()
    filename = exc_tb.tb_frame.f_code.co_filename

    error_message = "error occured and the file name is [{0}], at line number [{1}] and the error is [{2}]".format(
        filename, exc_tb.tb_lineno, str(error)
    )

    return error_message


class SensorException(Exception):
    def __init__(self, error_message, error_details: sys):
        super().__init__(error_message)
        
        self.error_message = error_message_details(
            error_message, error_details=error_details)

    def __str__(self):
        return self.error_message
