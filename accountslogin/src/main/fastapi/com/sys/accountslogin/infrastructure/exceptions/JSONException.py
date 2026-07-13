from fastapi import HTTPException, Response
import json

class JSONException(HTTPException):
    def __init__(self, message, status_code=400):
        super().__init__(status_code=status_code, detail=message)
        self.message = message
        self.status_code = status_code

    def to_http_response(self):
        response_data = {"status": "error", "message": self.message}
        return Response(content=json.dumps(response_data), media_type="application/json", status_code=self.status_code)
