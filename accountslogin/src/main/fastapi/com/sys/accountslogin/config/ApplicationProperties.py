
import os
import logging
from pathlib import Path
from typing import Callable
# Assuming the application_properties.py is in the same directory or appropriately available in the PYTHONPATH


class ApplicationProperties:
    def __init__(self):
        
        self.properties = {}

        self.properties_file='application.properties'
        self.load_properties(self.get_resources_path()+self.properties_file)
        self.logger = logging.getLogger(__name__)
    
    def get_resources_path(self):
        # Get the current file path
        current_file_path = Path(__file__)
        # Get the project directory path
        project_dir = current_file_path.parent.parent.parent.parent.parent.parent
        print(f"Current file path: {current_file_path}")
        print(f"Project directory: {project_dir}")
        return str(project_dir).replace("\\","/")+"/resources/"
    
    def load_properties(self, filepath):
        
        """Load properties from a file."""
        print(f"Resources application.properties: {filepath}")
        with open(filepath) as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    key, value = line.split('=', 1)
                    self.properties[key.strip()] = self.convert_value(value.strip())

    def get_property(self, key, default=None) ->Callable:
        # Iterating over all items in the properties dictionary
        for k, v in self.properties.items():
            if k == key:
                return v
        return default

    @staticmethod
    def convert_value(value):
        """Convert string values to their actual data types."""
        if value.lower() in ('true', 'false'):
            return value.lower() == 'true'
        try:
            return int(value)
        except ValueError:
            pass
        return value

    @property
    def AppDatasourceUrl(self):
        return self.get_property('app.datasource.url', 'defaultKey')

    @property
    def SecurityContentKey(self):
        return self.get_property('security.content.key', 'defaultKey')

    @property
    def SecurityJwtEnable(self):
        value = self.get_property('security.jwt.enable', True)
        return value
    
    @property
    def FilterSqlEnable(self):
        value = self.get_property('filter.sql.enable', True)
        return value
    

    @property
    def VerificationTokenHeaderName(self):
        value = self.get_property('verification.token.header.name','X-CSRFToken')
        return value

    @property
    def FilterSqlEnable(self):
        return self.get_property("filter.sql.enable", True)

    @property
    def AppName(self):
        return self.get_property("app.name", "FastAPI Application")
    
    @property
    def ContextPath(self):
        return self.get_property("context.path", "domain")
    
    def getAppName(self, b_quotes=False):
        # Directly accessing the variable from application_properties.py
        app_name = self.get_property("app.name", "FastAPI Application")
        self.logger.info(f"Loading the appName: {app_name}")
        if b_quotes:
            return f'"{app_name}"'
        return app_name

