from langchain.llms import OpenAI

# Set your OpenAI API key (you need to set your OpenAI API key in your environment variable)
import os
os.environ["OPENAI_API_KEY"] = "your-new-valid-api-key-here"


# Initialize the OpenAI LLM model
llm = OpenAI(temperature=0.5)

# Pass a prompt to the model and get the response
response = llm("Say Hello, World!")
print(response)
