from fastapi import FastAPI, Request

from ...http.WebRequest import WebRequest
from .csrf_token import csrf_token

from ....config.ApplicationProperties import ApplicationProperties

class csrf_token_element:
    ele_html=""
    csrf_token_value=""
    def __init__(self,request: WebRequest):
        applicationProperties=ApplicationProperties()
        # Generate CSRF token
        self.csrf_token_value = csrf_token(applicationProperties.SecurityContentKey)

        # Save the CSRF token in the session for later validation
        request.http_request.session['csrf_token'] = self.csrf_token_value
        
        # Generate HTML element with CSRF token
        self.ele_html = f'<input type="hidden" name="__RequestVerificationToken" data-custom="value" value="{self.csrf_token_value}">'
        self.ele_html += '<input type="hidden" id="verification_token_header_name" name="verification_token_header_name" value="'+applicationProperties.VerificationTokenHeaderName+'">'
    
    @property
    def get_csrf_token_value(self):
        return self.csrf_token_value
    
    @property
    def get_ele_html(self):
        return self.ele_html

