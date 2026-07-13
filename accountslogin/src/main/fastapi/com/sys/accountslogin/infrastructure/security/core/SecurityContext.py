import json
from .Authentication import Authentication


class SecurityContext:
    def __init__(self, authentication=None):
        self._authentication = authentication

    def get_authentication(self):
        return self._authentication

    def set_authentication(self, authentication):
        self._authentication = authentication

    def to_json(self):
        """
        Serializes the SecurityContext, including the nested Authentication object.
        """
        return json.dumps({
            'authentication': self._authentication.to_json() if self._authentication else None
        })
    
    @staticmethod
    def from_json_str(json_str):
        """
        Deserializes a JSON string to a SecurityContext object, including the nested Authentication object.
        """
        authentication = Authentication.from_json_str(json_str) if json_str else None
        return SecurityContext(authentication)
