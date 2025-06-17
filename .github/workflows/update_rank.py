import requests
from bs4 import BeautifulSoup
import re

GITHUB_USERNAME = "FistonSphere"
README_PATH = "README.md"

def fetch_rank(username):
    url = "https://committers.top/rwanda_private"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    rows = soup.select("table tbody tr")

    for i, row in enumerate(rows, start=1):
        if username.lower() in row.text.lower():
            return i
    return None

def update_readme(rank):
    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    new_line = f"🏅 Currently ranked **#{rank}** on [committers.top](https://committers.top/rwanda_private) 🇷🇼"
    pattern = r"🏅 Currently ranked \*\#\d+\* on \[committers\.top\]\(https:\/\/committers\.top\/rwanda_private\) 🇷🇼"
    updated = re.sub(pattern, new_line, content)

    if content != updated:
        with open(README_PATH, "w", encoding="utf-8") as f:
            f.write(updated)
        return True
    return False

if __name__ == "__main__":
    rank = fetch_rank(GITHUB_USERNAME)
    if rank:
        changed = update_readme(rank)
        print(f"Updated rank to #{rank}" if changed else "No change in rank.")
    else:
        print("Username not found.")
