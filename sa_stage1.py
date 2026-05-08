from openai import OpenAI
from openai import RateLimitError
import dotenv
import os

dotenv.load_dotenv()

# set up the openai client
client = OpenAI(
    api_key=os.getenv("LITELLM_API_KEY"),
    base_url=os.getenv("LITELLM_BASE_URL")
)

# set up tools
tools = [
    {
        "type": "mcp",
        "server_label": "AlphaVantage",
        "server_description": "Enables LLMs to interact with real-time and historical stock market data.",
        "server_url": "https://mcp.alphavantage.co/mcp",
        "require_approval": "never",
        "authorization": os.getenv("ALPHAVANTAGE_API_KEY")
    }
]

# instructions
with open("instructions.txt", "r", encoding="utf-8") as f:
    instructions = f.read()

# request
try:
    response = client.responses.create(
        model="gpt-4o-mini",
        input="Retrieve the last 3 days of daily data for 'APPL'",
        instructions=instructions,
        tools=tools
    )
    #print(response.output_text)
    print(response.output)

except RateLimitError as e:
    print(f"Rate limit hit: {e}")
