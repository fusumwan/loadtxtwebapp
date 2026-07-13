import asyncio
from sqlalchemy import Null
from asgiref.sync import sync_to_async
from asgiref.sync import async_to_sync

from ....infrastructure.dependencies.db import *
from sqlalchemy.ext.asyncio import AsyncSession
# we need to update the AUTHENTICATION_BACKENDS[] setting in settings.py

class AccountAuthenticationBackend:
    async def authenticate(self, db: AsyncSession, username=None, password=None):
        try:



                return None
        except Exception as e:
            print(e)
            return None
    
    def get_user(self, account_id):
        account=Null
        try:

            return account
        except account is None:
            return None
