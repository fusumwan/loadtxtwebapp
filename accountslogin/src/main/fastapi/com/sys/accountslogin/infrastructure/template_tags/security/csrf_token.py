from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from ...security.CSRFTokenManager import CSRFTokenManager
def csrf_token(key:str) -> str:
    _csrfToken=CSRFTokenManager(key)
    return _csrfToken.generate_token() 