import json
from typing import Collection
from ....infrastructure.security.core.authority import SimpleGrantedAuthority


class Authentication:
    _authorities : Collection[SimpleGrantedAuthority]
    def __init__(self, principal=None, credentials=None, authorities=None, details=None, authenticated=False):
        self._principal = principal
        self._credentials = credentials
        self._authorities : Collection[SimpleGrantedAuthority] = authorities
        from ....domain.services.CustomUserDetails import CustomUserDetails
        self._details : CustomUserDetails= details
        self._authenticated = authenticated

    @property
    def principal(self):
        return self._principal

    @principal.setter
    def principal(self, value):
        self._principal = value

    @property
    def credentials(self):
        return self._credentials

    @credentials.setter
    def credentials(self, value):
        self._credentials = value

    @property
    def authorities(self) ->Collection[SimpleGrantedAuthority]:
        return self._authorities

    @authorities.setter
    def authorities(self, value: Collection[SimpleGrantedAuthority]):
        self._authorities = value
    
    def isContainAutority(self,authority:SimpleGrantedAuthority | None):
        if authority==None:
            return False
        
        for exist_authority in self.authorities:
            if exist_authority.get_authority()==authority.get_authority():
                return True

        return False

    @property
    def details(self):
        return self._details

    @details.setter
    def details(self, value):
        self._details = value

    @property
    def authenticated(self):
        return self._authenticated

    @authenticated.setter
    def authenticated(self, value):
        self._authenticated = value
    
    def to_json(self):
        """
        Serializes this instance to a JSON string.
        """
        return json.dumps({
            'principal': self.principal,
            'credentials': self.credentials,
            'authorities': [authority.to_json() for authority in self.authorities],
            'details': self.details.to_json(),
            'authenticated': self.authenticated  # Include the 'authenticated' property
        })

    @staticmethod
    def from_json_str(json_str):
        """
        Deserializes a JSON string to an Authentication object.
        """
        data_json = json.loads(json_str)
        print(data_json)
        authentication_json=json.loads(data_json['authentication'])
        details_json=authentication_json.get('details', None)
        from ....domain.services.CustomUserDetails import CustomUserDetails
        details=CustomUserDetails.from_json_str(details_json) if details_json else None
        principal_json=authentication_json.get('principal', None)
        credentials_json=authentication_json.get('credentials', None)
        authorities_json=authentication_json.get('authorities', None)
        authenticated = authentication_json.get('authenticated', False)
        authorities = [SimpleGrantedAuthority.from_json_str(auth_json) for auth_json in authorities_json]
        return Authentication(
            principal=principal_json,
            credentials=credentials_json,
            authorities=authorities,
            details=details,
            authenticated=authenticated
        )