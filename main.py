import requests
import address
from bs4 import BeautifulSoup


indeed_result = requests.get(address.INDEED_ADDRESS)

indeed_soup = BeautifulSoup(indeed_result.text, 'html.parser')

pagination = indeed_soup.find("div", {"class":"pagination"})

# print(pagination.prettify())


links = pagination.find_all("a")
# print(links)
pages = []


for link in links[0:-1]:
  pages.append(int(link.find("span").string))
print(pages[0:-1]) #-1 is not included
print(pages[-1])

max_page = pages[-1]
# pages.pop(-1)
# print(pages)
