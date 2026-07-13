# Assuming this is placed within the infrastructure/lang directory
from .RuntimeException import RuntimeException

class IllegalStateException(RuntimeException):

    def __init__(self, message=None, cause=None, enableSuppression=True, writableStackTrace=True):
        super().__init__(message, cause, enableSuppression, writableStackTrace)
