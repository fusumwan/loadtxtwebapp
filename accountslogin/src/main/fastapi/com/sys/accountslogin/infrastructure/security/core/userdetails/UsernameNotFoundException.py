# Assuming this is placed within the infrastructure/security/core/userdetails directory
from ..AuthenticationException import AuthenticationException

class UsernameNotFoundException(AuthenticationException):

    def __init__(self, message=None, cause=None, enableSuppression=True, writableStackTrace=True):
        # Correctly matching the superclass constructor signature
        super().__init__(message=message,cause=cause,enableSuppression=enableSuppression,writableStackTrace=writableStackTrace)
        
