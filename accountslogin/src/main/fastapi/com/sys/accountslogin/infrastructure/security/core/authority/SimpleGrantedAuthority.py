import json
from ...access.AccessDecisionManager import GrantedAuthority

class SimpleGrantedAuthority(GrantedAuthority):
    def __init__(self, role):
        if not role:
            raise ValueError("A granted authority textual representation is required")
        self.role = role

    def get_authority(self):
        return self.role

    def __eq__(self, other):
        if self is other:
            return True
        if isinstance(other, SimpleGrantedAuthority):
            return self.role == other.role
        return False

    def __hash__(self):
        return hash(self.role)

    def __str__(self):
        return self.role
    

    def to_json(self):
        """
        Serializes this instance to a JSON string.
        """
        return json.dumps(self.__dict__)

    @staticmethod
    def from_json_str(json_str):
        data = json.loads(json_str)
        if isinstance(data, dict):  # If data is already a dict, no need for further parsing
            return SimpleGrantedAuthority(data['role'])
        # Else, assuming the data is a string that needs to be loaded
        data = json.loads(data)
        return SimpleGrantedAuthority(data['role'])