import os
from dotenv import load_dotenv

# Load variables from the .env file
load_dotenv()

# Now your existing code continues below:
AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")

print(f"DEBUG API KEY: {os.getenv('AZURE_OPENAI_API_KEY')}")
print(f"DEBUG ENDPOINT: {os.getenv('AZURE_OPENAI_ENDPOINT')}")