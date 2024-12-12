import requests

url = "https://www.capitoltrades.com/_next/data/hQiDrmIu3vjPhnfmY_lh8/trades.json"
response = requests.get(url)
print(response.json())
