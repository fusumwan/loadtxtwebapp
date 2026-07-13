class CustomException(Exception):
    def __init__(self, message=None, cause=None, enableSuppression=True, writableStackTrace=True):
        super().__init__(message=message)
        self.cause = cause
        self.enableSuppression = enableSuppression
        self.writableStackTrace = writableStackTrace
        self.message = message

    def getMessage(self):
        return self.message

    def getCause(self):
        return self.cause

    def __str__(self):
        if self.message:
            return self.message
        return super().__str__()
