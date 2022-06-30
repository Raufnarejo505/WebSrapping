from bs4 import BeautifulSoup
import requests

html=requests.get("https://www.bbc.com/urdu")

soup=BeautifulSoup(html,'lxml')
jobs=soup.find('p',class_='bbc-22iqn0 e1ibkbh72')
print(jobs)





