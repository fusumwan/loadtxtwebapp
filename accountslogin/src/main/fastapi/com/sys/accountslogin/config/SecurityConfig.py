import logging

class SecurityConfig:
    _instance = None
    logger = logging.getLogger("SecurityConfig")
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SecurityConfig, cls).__new__(cls)
            cls.logger.info("A new instance of SecurityConfig was created.")
        return cls._instance

    @classmethod
    def getInstance(cls):
        if cls._instance is None:
            cls._instance = cls()  # This will invoke __new__
            cls.logger.info("An instance of SecurityConfig was requested and created.")
        return cls._instance

    @staticmethod
    def is_permit_all_page(url):
        permitted = True  # Assuming all pages are permitted for simplicity
        SecurityConfig.logger.info(f"Permission check for URL '{url}': {'allowed' if permitted else 'denied'}")
        return permitted
