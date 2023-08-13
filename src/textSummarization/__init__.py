import os
import sys
import logging
from datetime import datetime
import sys


logging_string = "[%(asctime)s] || %(filename)s || %(lineno)d || %(name)s || %(funcName)s() || %(lineno)s || %(levelname)s || %(message)s"

log_dir = 'logs'


def get_current_time_stamp():
    return f"{datetime.now().strftime('%Y%m%d%H')}"


log_file_path = os.path.join(
    log_dir, get_current_time_stamp(), 'running_logs.log')
os.makedirs(os.path.dirname(log_file_path), exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=logging_string,
    handlers=[
        logging.FileHandler(log_file_path),
        logging.StreamHandler(sys.stdout)
    ]
)


logger = logging.getLogger("TextSummarizerLogger")

# ========================================================================================================


def error_message_detail(error, error_detail: sys):
    """
    It returns the error message with the file name, try block line number, exception block line number
    and the error message

    :param error: The error message that was raised
    :param error_detail: sys
    :type error_detail: sys
    :return: The error message
    """

    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    try_block_line_no = exc_tb.tb_lineno
    Exception_block_line_no = exc_tb.tb_frame.f_lineno
    error_message = f"""Python Script :
    [{file_name}] 
    at try block line number : [{try_block_line_no}] and exception block line no : [{Exception_block_line_no}] 
    error message : 
    [{str(error)}]
    """
    return error_message


class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        """
        A constructor function that initializes the class.

        :param error_message: The error message that will be displayed to the user
        :param error_detail: This is the error message that you want to display
        :type error_detail: sys
        """
        super().__init__(error_message)
        self.error_message = error_message_detail(
            error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message

    def __repr__(self) -> str:
        return CustomException.__name__.str()
