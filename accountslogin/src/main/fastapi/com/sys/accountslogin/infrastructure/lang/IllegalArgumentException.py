# Assuming this is placed within the infrastructure/lang directory
from .RuntimeException import RuntimeException

class IllegalArgumentException(RuntimeException):

    def __init__(self, message=None, cause=None):
        super().__init__(message, cause)
