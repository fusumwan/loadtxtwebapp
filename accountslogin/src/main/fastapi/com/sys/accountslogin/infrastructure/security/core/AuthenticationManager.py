# Adjusted the import statements to prevent circular imports and revised relevant sections of the code.


# In AuthenticationManager.py
# Ensure that any direct imports from CustomUserDetails or any file that might lead back to CustomUserDetailsService are carefully managed to avoid circular references.
# If a method requires CustomUserDetails, consider using a local import there as well.

from fastapi import APIRouter, Depends, HTTPException, Request, Form, status
from sqlalchemy.ext.asyncio import AsyncSession


from .Authentication import Authentication
from sqlalchemy.ext.asyncio import AsyncSession
from .AccountAuthenticationBackend import AccountAuthenticationBackend
class AuthenticationManager:
    def __init__(self):
        self.initialized = True
        self.accountAuthenticationBackend=AccountAuthenticationBackend()

    async def authenticate(self,db: AsyncSession,authentication: Authentication) -> Authentication:
        auth_obj = Authentication()
       
        return auth_obj

# Ensure all other class and method implementations are compatible with the adjustments made to avoid circular imports.
# This might involve revising how and where you import CustomUserDetails and related services across your application.
