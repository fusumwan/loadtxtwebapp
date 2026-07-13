
from sqlalchemy.ext.asyncio import AsyncSession


from accountslogin.src.main.fastapi.com.sys.accountslogin.infrastructure.security.core.Authentication import Authentication
from accountslogin.src.main.fastapi.com.sys.accountslogin.infrastructure.security.core.SecurityContext import SecurityContext
from ..infrastructure.dependencies.db import *
from .BaseController import BaseController  # Adjust the import path as necessary
from ..infrastructure.web.bind.decorator import *
from ..infrastructure.lang import *
from ..infrastructure.http import *

from ..infrastructure.template_tags.security import *


from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer
from starlette.requests import Request
from ..infrastructure.http import *



@RequestMapping("")
class HeaderController(BaseController):
    def __init__(self):
        super().__init__()  # Call the super class initializer to ensure it's properly initialized

    @RequestMapping("/header/", method = RequestMethod.GET, name="header")
    async def header(self, request: Request,db: AsyncSession = Depends(get_db)):
        request:WebRequest=WebRequest(request)
        self.logger.info("Entering header_get method in HeaderController.")
        return self.render(request,"header.html", self.context)

# Register the routes from the Webpage class
RegisterRoutes.getInstance().RegisterRoutes(HeaderController)