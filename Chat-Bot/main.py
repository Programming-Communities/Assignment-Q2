from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
import google.generativeai as genai
import os
import json
from datetime import datetime
from motor.motor_asyncio import AsyncIOMotorClient

# Load environment variables from .env
load_dotenv()

# Initialize FastAPI
app = FastAPI()

# MongoDB connection string
MONGO_URI = os.getenv("MONGO_URI")
if not MONGO_URI:
    raise ValueError("MongoDB connection string is missing!")

# MongoDB client setup
client: AsyncIOMotorClient = AsyncIOMotorClient(MONGO_URI)
db = client["chatbotDB"]

# Pydantic model for request body
class GeneratedContent(BaseModel):
    query: str
    response: str

# Initialize Google Generative AI model
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)
model_name = "gemini-1.5-flash"
model = genai.GenerativeModel(model_name)

# Route to generate content and save it to MongoDB and file
@app.post("/generate-and-save")
async def generate_and_save(query: str):
    # Generate content using Google Generative AI
    response = model.generate_content(query)
    
    # Prepare the data to be stored in MongoDB and the file
    data = {
        "query": query,
        "response": response.text,
    }
    
    # Save the data to MongoDB
    result = await db["messages"].insert_one(data)

    # Create a unique filename based on the current timestamp
    file_name = f"generated_content_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.json"
    file_path = os.path.join("generated_files", file_name)
    
    # Create the directory if it does not exist
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    # Save the data to a JSON file
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

    # Return the generated content and its MongoDB ID
    return {"id": str(result.inserted_id), "data": data, "file_path": file_path}

# Route to fetch saved messages (generated content)
@app.get("/messages")
async def get_messages():
    messages = await db["messages"].find().to_list(100)
    return messages

# Root route
@app.get("/")
async def read_root():
    return {"message": "Hello, FastAPI!"}
