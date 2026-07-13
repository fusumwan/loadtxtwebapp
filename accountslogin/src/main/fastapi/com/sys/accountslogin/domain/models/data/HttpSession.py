import logging
from fastapi import Request, HTTPException, status
from .SessionPersistence import SessionPersistence
class HttpSession:
    def __init__(self, request: Request):
        
        self._configure_logger()
        if 'session' not in request.scope:
            self.logger.error("Session middleware not configured.")
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Session middleware not configured.")
        self.logger.info("Session initialized successfully.")
        self.persistence = SessionPersistence.getInstance()
        # Ensure session key is set during initialization
        if 'session_key' not in request.scope['session']:
            request.scope['session']['session_key'] = self.generate_session_key()
            self.logger.info(f"New session key generated and set: {request.scope['session']['session_key']}")
        self._request = request
        pass
    def _configure_logger(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def generate_session_key(self):
        import uuid
        return str(uuid.uuid4())

    @property
    def session_key(self):
        if 'session' in self._request.scope:
            session_key = self._request.scope['session'].get('session_key', None)
            if session_key:
                self.logger.info(f"Session key retrieved: {session_key}")
                return session_key
            else:
                self.logger.error("Session key not available.")
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Session key not available.")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No session data found.")

    @property
    def attributes(self):
        return self._attributes
    
    @attributes.setter
    def attributes(self, value):
        self._attributes = value

    def has_key(self,value=None):
        if value is None:
            return False
        if 'session' in self._request.scope:
            keys_to_clear = list(self._request.scope['session'].keys())
            for attribute_name in keys_to_clear:
                if(self._request.scope['session'][attribute_name]==value):
                    return True
        return False

    def clear(self,attribute_name):
        if 'session' in self._request.scope and self.session_key:
            # Create a list of keys to iterate over to avoid RuntimeError
            keys_to_clear = list(self._request.scope['session'].keys())
            if attribute_name in keys_to_clear:
                del self._request.scope['session'][attribute_name]
                self.logger.info(f"Attribute '{attribute_name}' removed from session.")
    
    def is_contain_attribute(self,attribute_name):
        if 'session' in self._request.scope and self.session_key:
            if attribute_name in self._request.scope['session']:
                return True
        return False
    
    def get_attribute(self, attribute_name):
        if 'session' in self._request.scope and self.session_key:
            if attribute_name in self._request.scope['session']:
                return self._request.scope['session'][attribute_name]
            else:
                self.logger.error(f"Attribute '{attribute_name}' not found in session.")
                return None
        return None

    def set_attribute(self, attribute_name, attribute_value):
        if 'session' in self._request.scope and self.session_key:
            self._request.scope['session'][attribute_name] = attribute_value
            self.logger.info(f"Attribute '{attribute_name}' set with value: {attribute_value}")
        else:
            self.logger.error("Failed to set attribute, session data not accessible.")
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Session data not accessible.")

    def clear(self, attribute_name):
        if 'session' in self._request.scope and self.session_key:
            if attribute_name in self._request.scope['session']:
                del self._request.scope['session'][attribute_name]
                self.logger.info(f"Attribute '{attribute_name}' removed from session.")
        else:
            self.logger.error("Failed to remove attribute, session data not accessible.")
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Session data not accessible.")

    async def save(self):
        if 'session' in self._request.scope and self.session_key:
            session_data = self._request.scope['session']
            try:
                # Using the persistence layer to save session data
                self.persistence.setSession(self.session_key, session_data)
                self.logger.info("Session saved successfully.")
            except Exception as e:
                self.logger.exception("Failed to save session.")
                raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        else:
            self.logger.error("Session handling is not properly configured.")
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Session handling is not properly configured.")

    def remove_attribute(self, attribute_name):
        self.clear(attribute_name)