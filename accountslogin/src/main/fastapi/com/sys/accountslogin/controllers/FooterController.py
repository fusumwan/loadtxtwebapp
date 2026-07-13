from sqlalchemy.ext.asyncio import AsyncSession
from ..infrastructure.dependencies.db import *
from .BaseController import BaseController  # Adjust the import path as necessary
from ..infrastructure.web.bind.decorator import *
from ..infrastructure.lang import *
from ..infrastructure.http import *

@RequestMapping("")
class FooterController(BaseController):
    def __init__(self):
        super().__init__()  # Call the super class initializer to ensure it's properly initialized

    @RequestMapping("/footer/", method = RequestMethod.GET, name="footer")
    async def footer(self, request: Request,db: AsyncSession = Depends(get_db)):
        request:WebRequest=WebRequest(request)
        # Directly use self.contextPath initialized in BaseController
        self.logger.info("Entering footer_get method in FooterController.")
        return self.render(request,"footer.html", self.context)

# Register the routes from the Webpage class
RegisterRoutes.getInstance().RegisterRoutes(FooterController)