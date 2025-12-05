from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware # Import CORSMiddleware
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = FastAPI(
    title="Integrated RAG Chatbot API",
    description="Backend for the Physical AI & Humanoid Robotics Course RAG Chatbot, Personalization, and Translation features.",
    version="0.0.1",
)

# Get CORS origins from environment variables
cors_origins_str = os.getenv("CORS_ORIGINS", "")
origins = [origin.strip() for origin in cors_origins_str.split(',') if origin.strip()]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add AuthMiddleware
app.add_middleware(AuthMiddleware)

# Include API routers
app.include_router(chat.router)

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Integrated RAG Chatbot API!"}

# Example of how to access environment variables
# DB_URL = os.getenv("DATABASE_URL")
# print(f"Database URL: {DB_URL}")
