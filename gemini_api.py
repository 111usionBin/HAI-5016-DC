from dotenv import load_dotenv
import os
from google import genai

# Load `.env` from the repository root (if present) and read the key.
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise SystemExit("Missing GEMINI_API_KEY in environment or .env. Add GEMINI_API_KEY=<your_key> and rerun.")

# Pass the key explicitly to the client to avoid ambiguous credential lookup.
client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Explain how AI works in a few words",
)

print(response.text)