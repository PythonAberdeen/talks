# import our libraries

import requests
from bs4 import BeautifulSoup
url = "https://www.transport.gov.scot/publication/key-reported-road-casualties-scotland-2018/3-reported-numbers-of-accidents-table-1/"
year = "2017"
fatalities = ""

r = requests.get(url)

soup = BeautifulSoup(r.content,"html.parser")

table = soup.find('table', id='Table1')

rows = soup.find("table").find("tbody").find_all("tr")

for row in rows:
    cells = row.find_all("th")
    if cells[0].find("p").get_text() == year:
        data_cells = row.find_all("td")
        fatalities = data_cells[0].find("p").get_text()

print()
print(f"The number of fatalities in {year} was {fatalities}")

