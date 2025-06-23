import requests
from bs4 import BeautifulSoup
import pandas as pd


url = "	https://news.ycombinator.com/"
response = requests.get(url)
response.raise_for_status() 


soup = BeautifulSoup(response.text, "html.parser")


titles = []
links = []

for item in soup.select(".athing"):
    title_tag = item.select_one(".titleline > a")
    if title_tag:
        titles.append(title_tag.get_text())
        links.append(title_tag["href"])

df = pd.DataFrame({"Title": titles, "Link": links})
df.to_csv("hackernews_headlines.csv", index=False)

print("Scraping complete. Data saved to 'hackernews_headlines.csv'")
