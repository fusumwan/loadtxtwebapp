import secrets
from fastapi import HTTPException, Request

class CSRFTokenManager:
    def __init__(self, secret_key: str = "your_secret_key_here", token_length: int = 32):
        self.secret_key = secret_key
        self.token_length = token_length

    def generate_token(self) -> str:
        """
        Generate a CSRF token.
        """
        return secrets.token_urlsafe(self.token_length)

    def verify_token(self, token: str, request: Request):
        """
        Verify the CSRF token from the request against the one stored in session.
        """
        session_token = request.session.get("csrf_token")
        if not session_token or session_token != token:
            raise HTTPException(status_code=403, detail="CSRF token invalid or missing.")
