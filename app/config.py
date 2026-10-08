import os
from dotenv import load_dotenv
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")   # api key get from env
# print("name",GEMINI_API_KEY)
GEMINI_MODEL = os.getenv(
    "GEMINI_MODEL",      #get from env
    "gemini-3.6-flash"  # gemini default model
)
APP_NAME = os.getenv("APP_NAME", "Enterprise Agentic RAG")

if GEMINI_API_KEY:
    pass
else:
    raise ValueError("GEMINI_API_KEY is missing. "
       "Please configure it in your .env file.")