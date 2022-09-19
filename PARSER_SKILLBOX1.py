
import requests
from bs4 import BeautifulSoup

skillbox_response=requests.get("https://live.skillbox.ru/")
print(skillbox_response.status_code)

skillbox_content = skillbox_response.content
skillbox_soup = BeautifulSoup(skillbox_content)
titles = skillbox_soup.findAll(class_="webinar-card__title")

for title in titles:
  print(title.string.strip())