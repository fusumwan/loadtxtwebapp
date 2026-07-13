# Assuming this is placed within the infrastructure/lang directory
from ...lang.RuntimeException import RuntimeException


class AuthenticationException(RuntimeException):

    def __init__(self, message=None, cause=None, enableSuppression=True, writableStackTrace=True):
        # Correctly matching the superclass constructor signature
        #super().__init__(message=message,cause=cause,enableSuppression=enableSuppression,writableStackTrace=writableStackTrace)
        pass
