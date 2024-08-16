import requests
from config import NEWS_URL

def fetch_latest_news():
    try:
        response = requests.get(NEWS_URL)
        response.raise_for_status()
        data = response.json()
        return data.get("articles",[])
    except requests.RequestException as e:
        print(f"Failed to fetch news: {e}")
        return []