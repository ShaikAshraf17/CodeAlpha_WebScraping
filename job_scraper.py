import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://realpython.github.io/fake-jobs/"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

jobs = []

for card in soup.find_all("div", class_="card-content"):
    title = card.find("h2").text.strip()
    company = card.find("h3").text.strip()
    location = card.find("p", class_="location").text.strip()

    jobs.append({
        "Title": title,
        "Company": company,
        "Location": location
    })

df = pd.DataFrame(jobs)

df.to_csv("data/jobs.csv", index=False)

print(df.head())
print(f"\nTotal Jobs Scraped: {len(df)}")