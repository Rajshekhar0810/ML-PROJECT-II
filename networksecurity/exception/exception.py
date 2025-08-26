import sys    
from networksecurity.logging import logger


def error_message_details(error,error_detail: sys):  
    _,_,exc_tb = error_detail.exc_info()
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
        exc_tb.tb_frame.f_code.co_filename,
        exc_tb.tb_lineno,str(error)
    )  
    
    return error_message


class NetworkSecurityException(Exception):    # Custom exception class that inherits from the built-in Exception class.
    def __init__(self,error_message,error_detail: sys):
        super().__init__(error_message)  # Call the parent class constructor with the error message.
        self.error_message = error_message_details(error_message,error_detail)  # Store the formatted error message.

    def __str__(self):
        return self.error_message

# if __name__ == "__main__":
#     try:
#         logger.logging.info("Enter the try block")
#         a = 1/0
#     except Exception as e:
#         raise NetworkSecurityException(e,sys)