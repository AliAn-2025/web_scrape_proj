from bs4 import BeautifulSoup
import requests
from pprint import pprint

user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.10 Safari/605.1.1"

url = "https://www.scrapethissite.com/pages/forms/"
headers = {"User-Agent": user_agent}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, features='html.parser')

with open("web_scrape_practice.csv", 'w') as file:

    # Title columns
    row = []
    for title in soup.find_all('th'):
        print(title)
        title = title.text.strip()
        row.append(title)
    file.write(','.join(row))

team_names = []
years = []
wins = []
losses = []
ot_losses = []
win_percent = []
gf = []
ga = []
difference = []

with open("web_scrape_practice.csv", "r") as file:
    pass

print(soup.find_all('td'))
for td in soup.find_all('td'):
    print(f">{td.text.strip()}<")