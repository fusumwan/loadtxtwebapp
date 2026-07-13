from fastapi import Request
from starlette.datastructures import URL, Headers, FormData, QueryParams, UploadFile

from ...domain.models.data.HttpSession import HttpSession
from ..security.core.models.AnonymousUser import AnonymousUser
from ..security.core.baseuser.AbstractBaseUser import AbstractBaseUser
from typing import Union

class WebRequest:
    _request : Request = None
    _session : HttpSession = None
    _user :  Union[AbstractBaseUser, AnonymousUser] = None
    def __init__(self, request: Request):
        self._request : Request = request
        self._session : HttpSession =HttpSession(request)
        self._user : Union[AbstractBaseUser, AnonymousUser] = None

    @property
    async def body(self):
        # In FastAPI, to access the body, you must await it.
        return await self._request.body()
    
    async def build_absolute_uri(self, location: str = "") -> str:
        if not location:
            location = str(self._request.url)
        return str(URL(self._request.url).include_path(False).replace(path=location))

    @property
    def base_url(self) -> str:
        return self._request.base_url

    @property
    def session(self) -> HttpSession:
        # Sessions in FastAPI need custom implementation, typically using middleware
        if self._session is None and self._request is not None:
            self._session=HttpSession(self._request)
        return self._session
    
    @session.setter
    def session(self, value : HttpSession):
        self._session = value
    
    @property
    def user(self) -> Union[AbstractBaseUser, AnonymousUser]:
        # Ensure you have a dependency that injects the user into the request
        return self._user
    
    @user.setter
    def user(self, value : Union[AbstractBaseUser, AnonymousUser]):
        self._user = value
    
    @property
    def http_request(self) -> Request:
        return self._request

    @property
    def GET(self) -> QueryParams:
        # GET parameters are available as a QueryParams object
        return self._request.query_params
    
    @property
    def POST(self) -> FormData:
        # POST data in FastAPI is accessed differently, often via form() or json()
        return self._request.form()
    
    @property
    def COOKIES(self):
        # Cookies are directly accessible as a dict
        return self._request.cookies
    
    @property
    def META(self):
        # Meta information can be accessed via headers or other properties
        return Headers(self._request.headers)
    
    @property
    def FILES(self):
        # Files in FastAPI need to be handled through UploadFile objects
        return self._request.files
    
    @property
    def path(self):
        return self._request.url.path

    @property
    def method(self):
        return self._request.method
    
    @property
    def resolver_match(self):

        return None
    
    @property
    def content_type(self):
        return self._request.headers.get('content-type')

    @property
    def content_params(self):

        return None

    def clear(self):
        # Clearing or resetting the request object needs careful handling in async
        self._request = None
