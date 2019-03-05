import requests
from bs4 import BeautifulSoup

from app_db import Events, s

url = 'https://elbrusboot.camp/'

page = requests.get(url).text

soup = BeautifulSoup(page, 'lxml')

events = soup.find(class_="thisweek-wrap")  # <class 'bs4.element.Tag'>
# print(events.find_all('a').text)
for event in events.find_all('a'):
    print(event.find(class_="name").text, event.find(class_='date').text.strip(), event.get('href').strip())
    qwe = Events(name=event.find(class_="name").text, date=event.find(class_='date').text.strip(), link=event.get('href').strip())
    s.add(qwe)
s.commit()
