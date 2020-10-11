# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from requests import get
from urllib.request import Request, urlopen
import webbrowser

def get_articles():
    url = 'https://www.wsj.com/'
    response = urlopen(Request(url, headers={'User-Agent': 'Mozilla/5.0'}))
    soup = BeautifulSoup(response.read(), features="lxml")

    articles = soup.find_all("div", {"class": "WSJTheme--headline--7VCzo7Ay"})
    headers = []

    for article in articles:
        headers.append(article.h3.a.text)

    return headers

def get_google_link(header):
    h = header.replace(' ', '+')
    url = "https://www.google.com/search?q=" + h
    response = urlopen(Request(url, headers={'User-Agent': 'Mozilla/5.0'}))
    soup = BeautifulSoup(response.read(), features="lxml")

    result = soup.find_all("div", {"class": "kCrYT"})[2]

    link = result.a['href'][7:].split("&")[0]
    name = result.text.split("»")[0].split("›")[0]
    date = soup.find_all("div", {"class": "kCrYT"})[3].text.split("·")[0]

    if date[0] != 'f':
        date = "null or not recent"

    return [date, name, link]

def get_google_links(headers):
    links = []
    for header in headers:
        try:
            links.append(get_google_link(header))
        except:
            pass

    return links
