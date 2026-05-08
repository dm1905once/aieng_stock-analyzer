import os
import dotenv
import requests

dotenv.load_dotenv()
API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")
url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=AAPL&apikey={API_KEY}"

response = requests.get(url)
data = response.json()

print(data)

