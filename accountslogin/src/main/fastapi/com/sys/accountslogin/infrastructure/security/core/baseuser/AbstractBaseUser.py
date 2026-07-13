from pydantic import BaseModel, EmailStr, validator
from typing import Optional
from passlib.context import CryptContext
from datetime import datetime, timedelta
import jwt

# Password hashing context setup
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class AbstractBaseUser(BaseModel):
    id: Optional[int] = None
    email: EmailStr
    password: str
    is_active: bool = True
    is_superuser: bool = False
    is_staff: bool = False
    last_login: Optional[datetime] = None

    class Config:
        orm_mode = True  # If you're using SQLAlchemy

    @validator('password', pre=True, always=True)
    def hash_password(cls, v):
        return pwd_context.hash(v)

    def set_password(self, password: str):
        self.password = pwd_context.hash(password)

    def check_password(self, password: str) -> bool:
        return pwd_context.verify(password, self.password)

    def generate_jwt_token(self):
        # Example JWT token generation, adjust as per your application requirements
        token_expiry = datetime.utcnow() + timedelta(days=2)  # token expires in 2 days
        to_encode = {"exp": token_expiry, "sub": str(self.email)}
        encoded_jwt = jwt.encode(to_encode, "your-secret-key", algorithm="HS256")
        return encoded_jwt

    def last_login_now(self):
        self.last_login = datetime.now()

    def save(self, *args, **kwargs):
        # This method would interact with the database to save the user details.
        # Implement database interaction here.
        pass
