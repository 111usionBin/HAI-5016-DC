from dotenv import load_dotenv
import os
from datetime import date
from google import genai

# Load `.env` from the repository root (if present) and read the key.
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise SystemExit("Missing GEMINI_API_KEY in environment or .env. Add GEMINI_API_KEY=<your_key> and rerun.")

# Pass the key explicitly to the client to avoid ambiguous credential lookup.
client = genai.Client(api_key=api_key)

# Compute today's date and days until next Christmas (Dec 25)
today = date.today()
year = today.year
this_christmas = date(year, 12, 25)
if today <= this_christmas:
    next_christmas = this_christmas
else:
    next_christmas = date(year + 1, 12, 25)

days_until = (next_christmas - today).days

print(f"Today: {today.isoformat()}")
print(f"Days until next Christmas ({next_christmas.isoformat()}): {days_until}")
print('-----')
# Build a prompt that tells the LLM today's date and asks about weather near Christmas
prompt = (
    f"Today is {today.isoformat()}. There are {days_until} days until Christmas ({next_christmas.isoformat()}).\n"
    "Please provide a short summary (1-2 sentences) of the typical weather around Christmas in temperate regions, "
    "and one or two practical tips for clothing or travel preparations for that period."
)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt,
)

print("\nLLM response:\n")
print(response.text)

# Make a loop that asks for the user's input and sends it to the model until the user types 'exit'
while True:
    user_input = input("\nEnter your prompt (or type 'exit' to quit): ")
    if user_input.lower() == 'exit':
        print("Exiting the program.")
        break

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=user_input,
    )

    print("\nLLM response:\n")
    print(response.text)