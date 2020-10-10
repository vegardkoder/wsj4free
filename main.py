from bs4 import BeautifulSoup
from requests import get
from urllib.request import Request, urlopen

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
    print(h)
    url = "https://www.google.com/search?q=" + h
    response = urlopen(Request(url, headers={'User-Agent': 'Mozilla/5.0'}))
    soup = BeautifulSoup(response.read(), features="lxml")

    result = soup.find("div", {"class": "kCrYT"}).a

    print(result)

get_google_link("U.S. Covid-Testing Plan Aims to Open New York-London Travel by Holidays")
