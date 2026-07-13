from fastapi import FastAPI
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request

from accountslogin.src.main.fastapi.com.sys.accountslogin.config.ApplicationProperties import ApplicationProperties

app = FastAPI()

class BasePathMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, base_path=""):
        super().__init__(app)
        self.app_properties = ApplicationProperties()
        if base_path=="":
            base_path=self.app_properties.ContextPath
        self.base_path = base_path

    async def dispatch(self, request: Request, call_next):
        if request.url.path.startswith(self.base_path):
            request.scope["path"] = request.url.path[len(self.base_path) :]
        response = await call_next(request)
        return response



