from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv("config.env")

# Access the API key
api_key = os.getenv("GEMINI_KEY")
print(api_key)
