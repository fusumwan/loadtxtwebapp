# Assuming import paths based on your provided structure
from .Authentication import Authentication
from .AbstractAuthenticationToken import AbstractAuthenticationToken

class UsernamePasswordAuthenticationToken(AbstractAuthenticationToken):
    """
    An implementation of Authentication designed for a simple presentation of username and password.
    """
    authentication=None
    def __init__(self, username=None, password=None):
        super().__init__(username, password)
        self.authentication=Authentication()
        self.authentication.principal=username
        self.authentication.credentials=password
        # Setting the authenticated state to False initially
        self.authentication.authenticated=False

    # Implement or override methods from Authentication as necessary
    def get_principal(self):
        return self.authentication.principal

    def get_credential(self):
        return self.authentication.credentials

    def is_authenticated(self):
        return self.authentication.authenticated

    def set_authenticated(self, authenticated=True):
        self.authentication.authenticated=authenticated
    
    def instance(self) -> Authentication:
        return self.authentication

