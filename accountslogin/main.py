# main.py
import json
import re
from typing import Dict
from pydantic import BaseModel
from fastapi import Depends, FastAPI, Form, Request, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.ext.asyncio import AsyncSession

from accountslogin.src.main.fastapi.com.sys.accountslogin.infrastructure.dependencies.db import get_db
from .src.main.fastapi.com.sys.accountslogin.Application import Application
#In the controller, the route is indeed registered with the router as soon as Python reads and executes the class definition, specifically the @router.get("/") decorator. This happens before the app.include_router(router) call.
from .src.main.fastapi.com.sys.accountslogin.controllers import *
import uvicorn
# Ensure controllers are imported and instantiated as needed
# This could be where you previously called route_load()


# http://localhost:8000/
app_instance = Application.getInstance()
app_instance.middleware()
app_instance.configure()
app = app_instance.getApp()




'''

# Define a Pydantic model to parse and validate the request body
class UserCredentials(BaseModel):
    username: str
    password: str

@app.post("/accountslogin/authenticateTheUser2/")
async def authenticate_user(credentials: UserCredentials, request: Request):
    # Here, you'd have your logic to authenticate the user
    # For example, check credentials.username and credentials.password against your database
    # This is just a placeholder to simulate an authentication process
    if credentials.username == "admin" and credentials.password == "admin":
        # Simulate JWT creation or any other success response you need
        response_data = {"message": "User authenticated successfully", "token": "fake-jwt-token"}
        return JSONResponse(status_code=status.HTTP_200_OK, content=response_data)
    else:
        # If authentication fails, return an error response
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")




class UserCredentials(BaseModel):
    username_00: str
    password_01: str
    Limit: int



@app.post("/accountslogin/account/getByAccountUsernamePassword3/")
async def getByAccountUsernamePassword3(request: Request):
    # Read the request body as bytes
    body_bytes = await request.body()
    # Decode bytes to string assuming the request body is UTF-8 encoded
    body_str = body_bytes.decode('utf-8')
    print(body_str)
    # Parse the string as JSON
    data = json.loads(body_str)

    # Validate and convert to Pydantic model
    credentials = UserCredentials(**data)

    return JSONResponse(content={"data": "success"}, status_code=200)

'''


class FormDataParser:
    def __init__(self, body_str: str):
        self.fields = self.parse_form_data(body_str)

    def parse_form_data(self, body: str) -> Dict[str, str]:
        # Adjusted regular expression to correctly parse the multipart/form-data format
        pattern = re.compile(
            r'Content-Disposition: form-data; name="([^"]+)"\r\n\r\n(.*?)\r\n',
            re.DOTALL
        )
        # Find all matches and create a dictionary from them
        matches = pattern.findall(body)
        return {name.strip(): value.strip() for name, value in matches}

    def get_field(self, field_name: str) -> str:
        """ Retrieve the value of a form field by name """
        return self.fields.get(field_name, '')
    

@app.post("/accountslogin/account/getByAccountUsernamePassword4/")
async def getByAccountUsernamePassword4(
    username_00: str = Form(...), 
    password_01: str = Form(...), 
    Limit: int = Form(0),  # Changed to 'int' assuming 'Limit' should be an integer and provided a default value
    request: Request =None,
    db: AsyncSession = Depends(get_db)):
    # Debug print statements to ensure that values are received correctly
    print(f"Username: {username_00}, Password: {password_01}, Limit: {Limit}")
    
    
    # Simulated check - replace with your actual logic to fetch and validate the user
    if username_00 == "admin" and password_01 == "admin123":
        return JSONResponse(content={"message": "User found", "username": username_00, "limit": Limit}, status_code=200)
    else:
        raise HTTPException(status_code=404, detail="User not found")


'''
# Usage in your FastAPI route
@app.post("/accountslogin/account/getByAccountUsernamePassword/")
async def getByAccountUsernamePassword(request: Request):
    body_bytes = await request.body()
    body_str = body_bytes.decode('utf-8')
    form_data = FormDataParser(body_str)

    username = form_data.get_field("username_00")
    password = form_data.get_field("password_01")
    Limit = form_data.get_field("Limit")
    method = form_data.get_field("_method")

    # Debug output to see what was parsed
    print(f"Method: {method}, Username: {username}, Password: {password}, Limit: {Limit}")

    # Further processing...

'''
'''
# Usage in your FastAPI route
@app.post("/accountslogin/account/getByAccountUsernamePassword/")
async def getByAccountUsernamePassword(request: Request,db: AsyncSession = Depends(get_db)):
    username=(await WebRequestUtil.Request(request)).setRequestParameter("username_00").toStr()
    password=(await WebRequestUtil.Request(request)).setRequestParameter("password_01").toStr()
    Limit=(await WebRequestUtil.Request(request)).setRequestParameter("Limit").toInteger()
    method=(await WebRequestUtil.Request(request)).setRequestParameter("_method").toStr()

    # Debug output to see what was parsed
    print(f"Method: {method}, Username: {username}, Password: {password}, Limit: {Limit}")

    # Further processing...

'''
# In case you need to set a CSRF token or handle sessions, consider integrating FastAPI's dependencies and middlewares for sessions

