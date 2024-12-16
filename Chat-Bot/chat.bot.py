import absl.logging
absl.logging.set_verbosity(absl.logging.INFO)
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Retrieve the API key from environment variable
api_key = os.getenv("GOOGLE_API_KEY")

# Configure the API
genai.configure(api_key=api_key)

model_name = "gemini-1.5-flash"
model = genai.GenerativeModel(model_name)

response = model.generate_content(" hi")

print(response)

