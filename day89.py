
# Learn web scrapping

import requests
from bs4 import BeautifulSoup
url ="https://www.udemy.com"
# response = requests.get("https://www.udemy.com")
# print(response.text)
r = requests.get(url)

soup = BeautifulSoup(r.text,'htmlparser')
print(soup.prettify())
for heading in soup.find_all("h2"):
    print(heading.txt)


    # learn web scrpping
