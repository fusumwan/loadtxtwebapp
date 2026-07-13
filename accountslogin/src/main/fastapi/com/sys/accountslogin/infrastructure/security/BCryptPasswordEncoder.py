from passlib.context import CryptContext

class BCryptPasswordEncoder:
    pwd_context=None
    def __init__(self):
        # Create a cryptographic context
        self.pwd_context=CryptContext(schemes=["bcrypt"], deprecated="auto")
        pass

    def encode(self,password: str):
        return self.pwd_context.hash(password)