import sys
from src.logger import logging

def error_message_detail(error,error_detail:sys):
    """Generates a detailed error message with file name, line number, and error description.
    
    Args:
        error: The error object.
        error_detail (sys): The sys module to access exception information.
    
    Returns:
        str: A formatted error message string containing the file name, line number, and error description.
    """
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
     file_name,exc_tb.tb_lineno,str(error))

    return error_message

    

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        """Initializes a custom error class with an error message and detailed error information.
        
        Args:
            error_message (str): A brief description of the error.
            error_detail (sys): Detailed error information, typically obtained from a sys.exc_info() call.
        
        Returns:
            None
        
        Raises:
            None
        """
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
    
    def __str__(self):
        """Returns a string representation of the object.
        
        Returns:
            str: The error message associated with this object.
        """
        return self.error_message
    


        