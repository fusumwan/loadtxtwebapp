from fastapi import FastAPI, APIRouter
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from .infrastructure.http.middleware.BasePathMiddleware import BasePathMiddleware
import uvicorn

class Application():
    _instance = None
    app = FastAPI()
    router = APIRouter()
    route_paths = []  # Will contain dicts of {"path": ..., "method": ...}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Application, cls).__new__(cls)
            # Initialize any other attributes your singleton needs here
        return cls._instance

    @classmethod
    def getInstance(cls):
        if cls._instance is None:
            cls._instance = cls()  # This will invoke __new__
        return cls._instance
    
    def getApp(self):
        return self.app
    
    def setApp(self, value):
        self.app = value

    def getRouter(self):
        return self.router

    def middleware(self):
        # You might need to adjust origins according to your requirements
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],  # Allows all origins
            allow_credentials=True,
            allow_methods=["*"],  # Allows all methods
            allow_headers=["*"],  # Allows all headers
        )
        # Setting up the context path for global
        self.app.add_middleware(BasePathMiddleware)

    def configure(self):
        #FastAPI serves static files using StaticFiles from starlette.staticfiles. 
        self.app.mount("/static", StaticFiles(directory="accountslogin/src/main/resources/static"), name="static")
        self.app.mount("/static", StaticFiles(directory="accountslogin/src/main/resources/uploads"), name="uploads")
        
        # Configure your secret key
        # IMPORTANT: Keep this secret key safe. It's used to encrypt session data.
        SECRET_KEY = "your_secret_key_here"
        # Add SessionMiddleware to your application
        self.app.add_middleware(SessionMiddleware, secret_key=SECRET_KEY)
    
    def addRoutepath(self, path, method):
        route_path = {"path": path, "method": method.upper()}  # Normalize method to uppercase for consistency
        if not self.isRoutepathContain(path, method):
            self.route_paths.append(route_path)

    def isRoutepathContain(self, path, method):
        for existing_route in self.route_paths:
            if existing_route["path"] == path and existing_route["method"].upper() == method.upper():
                return True
        return False
