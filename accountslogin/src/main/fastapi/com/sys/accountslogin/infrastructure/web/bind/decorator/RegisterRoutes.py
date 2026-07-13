from fastapi import FastAPI
from fastapi.responses import HTMLResponse, Response
from typing import Callable, Type, Optional
from .....config.ApplicationProperties import ApplicationProperties
from functools import wraps
from .....Application import Application

class RegisterRoutes:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(RegisterRoutes, cls).__new__(cls)
            # Initialize any other attributes your singleton needs here
        return cls._instance

    @classmethod
    def getInstance(cls):
        if cls._instance is None:
            cls._instance = cls()  # This will invoke __new__
        return cls._instance
    
    # Modified function to register all routes from a class to the FastAPI app, now considers response_class
    def RegisterRoutes(self,view_class: Type):
        app=Application.getInstance().getApp()
        app_properties = ApplicationProperties()
        if hasattr(view_class, "_route_config"):
            class_attr = getattr(view_class, "_route_config")
            if len(class_attr)>0:
                class_level_path=class_attr[0]["path"]
                for attr_name in dir(view_class):
                    attr = getattr(view_class, attr_name)
                    if callable(attr) and hasattr(attr, "_route_config"):
                        for config in attr._route_config:
                            class_level_path=class_level_path.strip('/')
                            path=("/"+class_level_path+"/"+config["path"].strip('/')) if class_level_path != "" else ""+"/"+config["path"].strip('/')
                            if (path!="/"):
                                path_slash=path+"/"
                            self.AppRouteRegister(path,view_class,attr_name,config["method"],config["response_class"])
                            if path!=path_slash:
                                self.AppRouteRegister(path_slash,view_class,attr_name,config["method"],config["response_class"])
                            
    def AppRouteRegister(self,path,view_class,attr_name,methods,response_class):
        app=Application.getInstance().getApp()
        if not Application.getInstance().isRoutepathContain(path=path,method=methods):
            Application.getInstance().addRoutepath(path=path,method=methods)
            print("Route path:"+path)
            app.add_api_route(
                path,
                getattr(view_class(), attr_name),  # Create an instance and get the method
                methods=[methods],
                response_class=response_class  # Now uses the response_class from the decorator
            )
        Application.getInstance().setApp(app)
    