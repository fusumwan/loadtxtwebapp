import json
import logging
import typing
from typing import Any
from os import PathLike
from fastapi import APIRouter, Depends, HTTPException, Request, Form, status
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
from sqlalchemy.ext.asyncio import AsyncSession
from ..infrastructure.dependencies.db import *
from starlette.background import BackgroundTask
from starlette.responses import Response
from starlette.types import Receive, Scope, Send
from starlette.templating import _TemplateResponse
from ..config.ApplicationProperties import ApplicationProperties
from fastapi.templating import Jinja2Templates
from ..domain.utils.JsonUtil import JsonUtil
from ..infrastructure.http import *
from ..infrastructure.template_tags.security import *

class BaseController:
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.app_properties = ApplicationProperties()
        self.context={}
        # Initialize templates for rendering HTML
        self.templates = Jinja2Templates(directory="accountslogin/src/main/webapp/WEB_INF/views")
        self.templates.env.globals["https_url_for"] = self.https_url_for

    def https_url_for(self,request: Request, name: str, **path_params: Any) -> str:
        # Generate the original URL
        http_url = request.url_for(name, **path_params)
        # Reconstruct the URL with the new scheme
        return http_url._url.replace("http://","https://")

    def set_context(self, request: WebRequest, context: dict ={}):
        base_path = str(request.base_url)
        
        csrf_element=csrf_token_element(request)
        request.session.set_attribute("csrf_token",csrf_element.csrf_token_value) # Storing token in session
        context=JsonUtil.set_properties(context,"request",request.http_request)
        return context
    
    def render(
        self,
        request: WebRequest,
        name: str,
        context: dict ={},
        status_code: int = 200,
        headers: typing.Optional[typing.Mapping[str, str]] = None,
        media_type: typing.Optional[str] = None,
        background: typing.Optional[BackgroundTask] = None,
    ) -> _TemplateResponse:
        context=self.set_context(request,context)
        return self.templates.TemplateResponse(name,context,status_code,headers,media_type,background)
