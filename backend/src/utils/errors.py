from fastapi import HTTPException, status
from typing import Optional # Import Optional

class DetailedHTTPException(HTTPException):
    """
    Custom HTTP exception with more detailed error messages.
    """
    def __init__(self, status_code: int, detail: str, error_code: Optional[str] = None):
        super().__init__(status_code=status_code, detail=detail)
        self.error_code = error_code

# Common error types
CREDENTIALS_EXCEPTION = DetailedHTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    error_code="AUTH_001"
)

USER_NOT_FOUND_EXCEPTION = DetailedHTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="User not found",
    error_code="USER_001"
)

# Add more specific exceptions as needed