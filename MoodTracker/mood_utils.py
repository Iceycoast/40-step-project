import json
from datetime import datetime
from dotenv import load_dotenv
import openai
import os 

openai.api_key = os.getenv("OPENAI_API_KEY")
