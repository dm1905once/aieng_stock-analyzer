from openai import OpenAI
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
        "allowed_tools": ["TOOL_CALL"],
        "authorization": os.getenv("ALPHAVANTAGE_API_KEY")
    }
]

# instructions
with open("instructions.txt", "r", encoding="utf-8") as f:
    instructions = f.read()

# request
response = client.responses.create(
    model="gpt-4o-mini",
    instructions=instructions,
    tools=tools,
    max_tool_calls=1,
    input="Retrieve the last 3 days of daily data for 'AAPL'"
)

print(response.output)
#print("====== Printing full response ============")
#print(response.model_dump_json(indent=2))
