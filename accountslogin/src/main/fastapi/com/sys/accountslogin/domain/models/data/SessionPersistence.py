import logging
#For FastAPI, which does not natively manage session persistence, session data typically needs to be explicitly managed and persisted, either to a memory storage system. 

class SessionPersistence:
    _instance = None
    logger = logging.getLogger("SessionPersistence")
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    session_map = {}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SessionPersistence, cls).__new__(cls)
            cls.logger.info("A new instance of SessionPersistence was created.")
        return cls._instance

    @classmethod
    def getInstance(cls):
        if cls._instance is None:
            cls._instance = cls()  # This will invoke __new__
            cls.logger.info("An instance of SessionPersistence was requested and created.")
        return cls._instance
    
    def setSession(self, session_key: str, value):
        self.session_map[session_key] = value
        self.logger.info(f"Session data for key {session_key} set successfully.")
    
    def getSession(self, session_key: str):
        if session_key in self.session_map:
            self.logger.info(f"Session data for key {session_key} retrieved successfully.")
            return self.session_map[session_key]
        self.logger.warning(f"No session data found for key {session_key}.")
        return None
