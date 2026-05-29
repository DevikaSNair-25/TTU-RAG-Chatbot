import requests
from bs4 import BeautifulSoup
import os

urls = [
    "https://ao.ttu.edu.tw/",
    "https://ao.ttu.edu.tw/p/412-1073-2399.php",
    "https://www.ttu.edu.tw/",
    "https://www.ttu.edu.tw/p/412-1001-1.php",
    "https://www.ttu.edu.tw/p/412-1001-2.php",
    "https://www.ttu.edu.tw/p/404-1001-1.php",
    "https://ao.ttu.edu.tw/p/412-1073-2400.php",
    "https://ao.ttu.edu.tw/p/412-1073-2401.php",
    "https://ao.ttu.edu.tw/p/412-1073-2402.php",
    "https://ao.ttu.edu.tw/p/412-1073-2403.php",
    "https://ao.ttu.edu.tw/p/412-1073-2404.php",
    "https://ao.ttu.edu.tw/p/412-1073-2405.php",
]

os.makedirs("data", exist_ok=True)

for i, url in enumerate(urls):
    try:
        print(f"Scraping: {url}")
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")
        text = soup.get_text()
        with open(f"data/page{i}.txt", "w", encoding="utf-8") as f:
            f.write(text)
    except Exception as e:
        print(f"Failed: {url} - {e}")

print("Done scraping")

