import os
from dotenv import load_dotenv
from qdrant_client import QdrantClient

load_dotenv() # Load environment variables from .env

QDRANT_URL = os.getenv("QDRANT_URL")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")

if not QDRANT_URL:
    raise ValueError("QDRANT_URL environment variable is not set.")

# Initialize Qdrant client
# For a local instance, you might just use QdrantClient(host="localhost", port=6333)
# For Qdrant Cloud, use the URL and API Key
qdrant_client = QdrantClient(
    url=QDRANT_URL,
    api_key=QDRANT_API_KEY,
)

def get_qdrant_client():
    return qdrant_client
