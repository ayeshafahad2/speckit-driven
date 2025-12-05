from fastapi import Request, Response, HTTPException, status
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.types import ASGIApp
from typing import Optional
import os

# In a real application, this would involve JWT decoding and validation
# For now, we'll simulate it.
class AuthMiddleware(BaseHTTPMiddleware):
    def __init__(self, app: ASGIApp):
        super().__init__(app)

    async def dispatch(self, request: Request, call_next):
        # Allow OPTIONS requests to pass through without auth check
        if request.method == "OPTIONS":
            return await call_next(request)

        # Skip auth for public endpoints (e.g., /auth/login, /auth/signup, /)
        public_endpoints = ["/", "/auth/login", "/auth/signup"]
        if request.url.path in public_endpoints or request.url.path.startswith("/docs"):
            response = await call_next(request)
            return response

        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Bearer "):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Not authenticated",
                headers={"WWW-Authenticate": "Bearer"},
            )

        token = auth_header.split(" ")[1]

        # Simulate token validation and user loading
        # In a real app, you'd decode JWT, validate signature, check expiration,
        # and fetch user from DB based on token payload.
        if token == "simulated_jwt_token":
            # Attach a simulated user to the request state
            request.state.user_id = "simulated-user-id"
            request.state.user_email = "simulated@example.com"
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid authentication token",
                headers={"WWW-Authenticate": "Bearer"},
            )

        response = await call_next(request)
        return response
