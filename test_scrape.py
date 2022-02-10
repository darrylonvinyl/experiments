import urllib3
from bs4 import BeautifulSoup
url = "https://lxml.de/installation.html"
ourUrl = urllib3.PoolManager().request('GET', url).data
soup = BeautifulSoup(ourUrl, "lxml")
print(soup.find('title').text)
