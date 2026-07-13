from fastapi import Response, status
from typing import Any, Dict
import json
import logging

'''

Type Checking: The constructor now checks if the provided content is a dictionary. This ensures the correct type of input is being passed to the class, avoiding errors during serialization.

Safety Checks: If the safe parameter is True, the ensure_safe_content method is called to inspect each item in the dictionary and ensure it can be serialized to JSON. Non-serializable items are converted to strings. This makes the class more robust by preventing serialization failures.

Error Handling: Added robust error handling around JSON serialization to catch and log serialization errors, raising an informative exception if serialization fails.

Logging: Enhanced logging capabilities are added to track operations within the class, aiding debugging and providing traceability of actions.

These improvements to the ResponseEntity class make it more robust and secure, suitable for various use cases where JSON responses are needed in a FastAPI application.

'''

class ResponseEntity(Response):
    logger = logging.getLogger("ResponseEntity")
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    def __init__(self, content: Dict[str, Any], safe: bool = False, status_code: int = 200):
        if not isinstance(content, dict):
            self.logger.error("Content must be a dictionary.")
            raise ValueError("Content must be a dictionary.")
        
        if safe:
            # Perform additional checks or transformations to ensure the dictionary is safe for JSON serialization
            content = self.ensure_safe_content(content)

        try:
            json_content = json.dumps(content)
        except TypeError as e:
            self.logger.exception("Failed to serialize content to JSON.")
            raise ValueError(f"Failed to serialize content to JSON: {str(e)}")

        super().__init__(
            content=json_content,
            media_type="application/json",
            status_code=status_code
        )

    def ensure_safe_content(self, content: Dict[str, Any]) -> Dict[str, Any]:
        """
        Ensures all values in the dictionary are safe for JSON serialization.
        This can involve converting non-serializable objects to strings or handling them appropriately.
        """
        safe_content = {}
        for key, value in content.items():
            try:
                # Attempt to serialize the value to JSON to check if it's safe
                json.dumps({key: value})
                safe_content[key] = value
            except TypeError:
                safe_content[key] = str(value)  # Convert non-serializable objects to string
                self.logger.warning(f"Converted non-serializable value for key '{key}' to string.")
        return safe_content
