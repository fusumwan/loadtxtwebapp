from fastapi import FastAPI
from fastapi.responses import HTMLResponse, Response
from typing import Callable, Type, Optional
from functools import wraps
from ..decorator import *


# Modified decorator factory to accept response_class and utilize it.
def RequestMapping(value: str, method: RequestMethod=RequestMethod.GET, consumes=None, produces=None, name=None, response_class: Type[Response] = HTMLResponse):
    def decorator(obj: Callable):
        path=value
        if not isinstance(obj, type):
            func_obj=obj
            @wraps(func_obj)
            async def wrapper(*args, **kwargs):
                return await func_obj(*args, **kwargs)

            # Attach route information to the function
            if not hasattr(func_obj, "_route_config"):
                func_obj._route_config = []
            func_obj._route_config.append({
                "path": path,
                "method": method.value,
                "consumes": consumes,
                "produces": produces,
                "name": name,
                "callback": wrapper,  # The actual function to be called by FastAPI
                "response_class": response_class  # Capture the response_class for use when registering the route
            })
            return func_obj
        else:
            class_obj=obj
            # Attach route information to the function
            if not hasattr(class_obj, "_route_config"):
                class_obj._route_config = []
            class_obj._route_config.append({
                "path": path
            })
            return class_obj
    return decorator