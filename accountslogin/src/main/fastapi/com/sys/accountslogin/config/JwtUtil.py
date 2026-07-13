import jwt
import datetime

class JwtUtil:
    def __init__(self):
        self._SECRET_KEY = "SENTENCE_WEB_SECRET_KEY"

    @property
    def SECRET_KEY(self):
        return self._SECRET_KEY

    @SECRET_KEY.setter
    def SECRET_KEY(self, value):
        self._SECRET_KEY = value

    def generate_token(self, username):
        payload = {
            'sub': username,
            'iat': datetime.datetime.utcnow(),
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=10)
        }
        return jwt.encode(payload, self._SECRET_KEY, algorithm='HS256')

    def validate_token(self, token):
        try:
            jwt.decode(token, self._SECRET_KEY, algorithms=['HS256'])
            return True
        except Exception as e:
            return False

    def extract_username(self, token):
        try:
            payload = jwt.decode(token, self._SECRET_KEY, algorithms=['HS256'])
            return payload['sub']
        except Exception as e:
            return None
