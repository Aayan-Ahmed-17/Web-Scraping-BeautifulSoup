import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

#all jobs cards | it holds div which contains every single job
# results = soup.find(id="ResultsContainer")
# job_cards = results.find_all("div", class_ = "card-content")