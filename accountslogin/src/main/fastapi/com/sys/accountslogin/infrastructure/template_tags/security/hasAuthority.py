from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer
from starlette.requests import Request

from ....infrastructure.http.WebRequest import WebRequest
from ....infrastructure.security.core.authority import SimpleGrantedAuthority
from ....infrastructure.security.core.Authentication import Authentication
from ....infrastructure.security.core.SecurityContext import SecurityContext
from ....domain.models.data.HttpSession import HttpSession


def hasAuthority(request: Request, authorithy_name: str) -> bool:
    request:WebRequest=WebRequest(request)

    return False

