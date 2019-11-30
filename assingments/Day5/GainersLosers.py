from requests import get
from bs4 import BeautifulSoup
url='https://www.moneycontrol.com/'
res=get(url)

bSoup=BeautifulSoup(res.text,'html.parser')

gainers = bSoup.find_all('div',attrs={'id':'tgNifty'})
print("Gainers Nifty")
for gainer in gainers:
    link = gainer.find_all('a')
    for link in link[:-1]:
        print(link.get('title'))
print("============================================")
losers = bSoup.find_all('div',attrs={'id':'tlNifty'})
print("Losers Nifty")
for loser in losers:
    link = loser.find_all('a')
    for link in link[:-1]:
        print(link.get('title'))
print ("===========================================")
losers = bSoup.find_all('div',attrs={'id':'tlSensex'})
print("Losers Sensex")
for loser in losers:
    link = loser.find_all('a')
    for link in link[:-1]:
        print(link.get('title'))
print("============================================")
gainers = bSoup.find_all('div',attrs={'id':'tgSensex'})
print("Gainers Sensex")
for gainer in gainers:
    link = gainer.find_all('a')
    for link in link[:-1]:
        print(link.get('title'))

