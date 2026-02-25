import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

# all jobs cards | it holds div which contains every single job
results = soup.find(id="ResultsContainer")
job_cards = results.find_all("div", class_="card-content")
# for job_card in job_cards:
#     title = job_card.find("h2", class_ = "title")
#     company = job_card.find("h3", class_ = "company")
#     location = job_card.find("p", class_ = "location")
#     print(title.text.strip())
#     print(company.text.strip())
#     print(location.text.strip())
#     print()

# Want to find only python job instead of all 100 jobs
python_job_cards = results.find_all("h2", string=lambda text: "python" in text.lower())
for job in python_job_cards:
    print(job.text.strip())
