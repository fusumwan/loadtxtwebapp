import threading

from .SecurityContext import SecurityContext

_thread_local = threading.local()

class SecurityContextHolder:

    @staticmethod
    def get_context():
        """
        Returns the current security context for the current thread.
        """
        if not hasattr(_thread_local, 'security_context'):
            _thread_local.security_context = SecurityContext()
        return _thread_local.security_context
    @staticmethod
    def set_context(sc:SecurityContext):
        """
        Bind the SecurityContext to the current thread
        """
        _thread_local.security_context = sc
            
    @staticmethod
    def clear_context():
        """
        Clears the security context for the current thread.
        """
        if hasattr(_thread_local, 'security_context'):
            del _thread_local.security_context
