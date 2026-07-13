# RuntimeException.py, assuming Exception.py is in the same directory
from .CustomException import CustomException


class RuntimeException(CustomException):
    def __init__(self, message=None, cause=None, enableSuppression=True, writableStackTrace=True):
        super().__init__(message=message,cause=cause,enableSuppression=enableSuppression,writableStackTrace=writableStackTrace)
        


