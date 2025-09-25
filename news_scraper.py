import requests
from bs4 import BeautifulSoup

URL = "https://www.bbc.com/news"

response = requests.get(URL)
if response.status_code != 200:
    print("Failed to retrieve webpage")
    exit()

soup = BeautifulSoup(response.text, "html.parser")

headlines = []
for h in soup.find_all(['h2', 'h3']):
    text = h.get_text().strip()
    if text and len(text) > 10:
        headlines.append(text)

if not headlines:
    print("⚠️ No headlines found. The page structure may have changed.")
else:
    with open("headlines.txt", "w", encoding="utf-8") as f:
        for i, title in enumerate(headlines, 1):
            f.write(f"{i}. {title}\n")
    print(f"✅ {len(headlines)} headlines saved to headlines.txt")
