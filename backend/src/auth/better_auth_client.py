import os
from dotenv import load_dotenv
import httpx # For making HTTP requests to external API

load_dotenv() # Load environment variables from .env

BETTER_AUTH_API_KEY = os.getenv("BETTER_AUTH_API_KEY")
BETTER_AUTH_SECRET_KEY = os.getenv("BETTER_AUTH_SECRET_KEY")
BETTER_AUTH_BASE_URL = os.getenv("BETTER_AUTH_BASE_URL", "https://api.better-auth.com")

class BetterAuthClient:
    def __init__(self):
        if not BETTER_AUTH_API_KEY or not BETTER_AUTH_SECRET_KEY:
            raise ValueError("BetterAuth API Key or Secret Key not set in environment variables.")
        self.base_url = BETTER_AUTH_BASE_URL
        self.headers = {
            "X-API-Key": BETTER_AUTH_API_KEY,
            "X-Secret-Key": BETTER_AUTH_SECRET_KEY,
            "Content-Type": "application/json"
        }
        self.client = httpx.AsyncClient()

    async def signup(self, email: str, password: str, software_background: str = None, hardware_background: str = None):
        """Simulates user signup with Better-Auth.com."""
        payload = {
            "email": email,
            "password": password,
            "user_metadata": {
                "software_background": software_background,
                "hardware_background": hardware_background
            }
        }
        # In a real scenario, this would call Better-Auth.com's signup endpoint
        # response = await self.client.post(f"{self.base_url}/signup", json=payload)
        # response.raise_for_status()
        # return response.json()
        print(f"Simulating signup for {email} with metadata: {payload['user_metadata']}")
        return {"user_id": "simulated-user-id", "email": email, "message": "Simulated signup successful"}

    async def login(self, email: str, password: str):
        """Simulates user login with Better-Auth.com."""
        payload = {
            "email": email,
            "password": password
        }
        # response = await self.client.post(f"{self.base_url}/login", json=payload)
        # response.raise_for_status()
        # return response.json()
        print(f"Simulating login for {email}")
        return {"user_id": "simulated-user-id", "email": email, "access_token": "simulated_jwt_token"}

    async def get_user_profile(self, user_id: str, access_token: str):
        """Simulates fetching user profile from Better-Auth.com."""
        # response = await self.client.get(f"{self.base_url}/users/{user_id}", headers={"Authorization": f"Bearer {access_token}"})
        # response.raise_for_status()
        # return response.json()
        print(f"Simulating fetching profile for user_id: {user_id}")
        return {
            "user_id": user_id,
            "email": "simulated@example.com",
            "user_metadata": {
                "software_background": "Simulated Python developer",
                "hardware_background": "Simulated NVIDIA user"
            }
        }

    # Add more methods as needed, e.g., logout, update_user_metadata etc.

better_auth_client = BetterAuthClient()
