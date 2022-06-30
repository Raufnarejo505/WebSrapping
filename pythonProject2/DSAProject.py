from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd


# url='https://www.bbc.com/urdu/topics/cjgn7n9zzq7t';
# res=requests.get(url)
# html=res.content
# soup=BeautifulSoup(html,'lxml')
#
#
# story=soup.find_all('div',class_='bbc-bjn8wh e3hd7yi2')
#
# for item in story:
#     head=item.h2.a.text
#     print(head)



# article=soup.find('article')
# headline=soup.h2.a['href']


# print(article.prettify())

# navg=soup.find_all('li',class_='bbc-22iqn0 e1ibkbh72')
#
# for item in navg:
#     tag=item.a.text
#     print(tag)


# pakistan=soup.find_all('li',class_='bbc-n8va9n euuxl8v1')
# for item in pakistan:
#     headline=item.h2.a.text
#     print(headline)



# spantag=soup.find_all('div',class_='bbc-1rgju53 ezqrok41')
#
# for item in spantag:
#     tag=item.find('span',class_="bbc-997krp e10c375a1")
#     print(tag.text)


# next=soup.find_all('li',class_='essoxwk0 bbc-1tx9q9n e1xplp7e1')
#
# News=soup.find_all('div',class_='bbc-1ehn615 eivmfr65')
#
# for item in next:
#     headline=item.h3.a.text
#     print(headline)


# with open('ExcelSheet2.csv', 'w', newline='') as f:
#     ff = csv.writer(f)
#     header = ['HeadLine ', 'Story']
#     ff.writerow(header)

# for items in News:
#     headline = items.h3.a.text
#     print("HeadLine"+headline)
#     print()
#     paragraph = items.find('p', class_='bbc-9hhp09 eivmfr61').text
#     print(paragraph)



# pakurl='https://www.bbc.com/urdu/topics/cjgn7n9zzq7t';
# ress=requests.get(pakurl)
# html22=ress.content
# soup2=BeautifulSoup(html22,'lxml')
#
#
# story=soup2.find_all('div',class_='bbc-bjn8wh e3hd7yi2')
#
# print('pakistan stories\n')
#
# for item in story:
#     head=item.h2.a.text
#     print(head)

# print('\n\n World sotries\n\n')
#
# worldurl='https://www.bbc.com/urdu/topics/c340q0p2585t';
# res2=requests.get(worldurl)
# html3=res2.content
# soup3=BeautifulSoup(html3,'lxml')
#
#
# story3=soup3.find_all('div',class_='bbc-bjn8wh e3hd7yi2')
#
#
#
# for item in story3:
#     head=item.h2.a.text
#     print(head)
#


category = 'https://www.bbc.com/urdu/topics/cjgn7n9zzq7t'

page = requests.get(category + "/page/" + str(1)).text

            # print(page)
soup = BeautifulSoup(page, 'lxml')

articles = soup.find('article', class_='qa-post gs-u-pb-alt+ lx-stream-post gs-u-pt-alt+ gs-u-align-left')
headline = articles.find('span', class_='lx-stream-post__header-text gs-u-align-middle').text

read_more = articles.find('a', class_='qa-story-cta-link')

read_more_link = read_more['href']

url='https://www.bbc.com/' + read_more_link
# print(url)

res=requests.get(url)
html=res.content
# soup=BeautifulSoup(html,'lxml')
soup_2 = BeautifulSoup(html, 'lxml')
paragraphs = soup_2.find_all('div', class_='bbc-4wucq3 essoxwk0')
for par in paragraphs:
    #pa=par.find('p',class_='bbc-yabuuk e1cc2ql70')
    print(par.text)
    print()
