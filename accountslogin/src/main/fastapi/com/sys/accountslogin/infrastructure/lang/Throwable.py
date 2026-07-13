from re import L
from ..io.Serializable import Serializable
from . import *


class Throwable(Serializable):
    UNASSIGNED_STACK = []

    def __init__(self, message=None, cause=None, enableSuppression=True, writableStackTrace=True):
        super().__init__()
        self.detailMessage = message
        self.cause = cause if cause is not None else self
        self.suppressedExceptions = [] if enableSuppression else None
        self.stackTrace = self.UNASSIGNED_STACK if writableStackTrace else None

    def getMessage(self):
        return self.detailMessage

    def getLocalizedMessage(self):
        return self.getMessage()

    def getCause(self):
        return None if self.cause == self else self.cause

    def initCause(self, cause):
        if self.cause is not self:
            raise IllegalStateException("Can't overwrite cause")
        if cause == self:
            raise IllegalArgumentException("Self-causation not permitted")
        self.cause = cause
        return self

    def toString(self):
        s = self.__class__.__name__
        message = self.getLocalizedMessage()
        return f"{s}: {message}" if message else s

    def printStackTrace(self):
        # Simulate Java's printStackTrace method in Python
        import traceback
        traceback.print_exc()

    def fillInStackTrace(self):
        import sys
        self.stackTrace = sys.exc_info()[2]
        return self

    def setStackTrace(self, stackTrace):
        self.stackTrace = stackTrace

    def addSuppressed(self, exception):
        if exception == self:
            raise IllegalArgumentException("Self-suppression not permitted")
        if self.suppressedExceptions is not None:
            self.suppressedExceptions.append(exception)

    def getSuppressed(self):
        return self.suppressedExceptions if self.suppressedExceptions else []




