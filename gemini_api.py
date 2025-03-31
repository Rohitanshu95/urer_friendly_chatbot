import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
API_KEY = os.getenv("AIzaSyC41VIkWqbwEL3iEexKWv1FZX2NFdHiy9k")

# Configure Gemini API
genai.configure(api_key=API_KEY)

def get_gemini_response(prompt):
    """Fetch response from Gemini AI."""
    model = genai.GenerativeModel("gemini-1.5-pro")  # FIXED MODEL NAME
    response = model.generate_content(prompt)
    return response.text
