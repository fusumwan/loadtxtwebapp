from .Authentication import Authentication
from .CredentialsContainer import CredentialsContainer

class AbstractAuthenticationToken(Authentication, CredentialsContainer):
    """
    Base class for Authentication objects, must be immutable.
    """
    def __init__(self, principal=None, credentials=None, authenticated=False):
        self._principal = principal
        self._credentials = credentials
        self._authenticated = authenticated

    def get_principal(self):
        return self._principal

    def get_credentials(self):
        return self._credentials

    def is_authenticated(self):
        return self._authenticated

    def set_authenticated(self, authenticated):
        if not isinstance(authenticated, bool):
            raise ValueError("authenticated must be a boolean value")
        self._authenticated = authenticated

    def erase_credentials(self):
        self._credentials = None
