# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 17:16:56 2018

@author: hp
"""


from urllib.request import urlopen
from bs4 import BeautifulSoup

url=urlopen("https://en.wikipedia.org/wiki/Comma-separated_values")
html1=BeautifulSoup(url.read(100000),"lxml")
parse=html1.find("div",{"class":"mw-headline"})
print(parse.text)


from urllib.request import urlopen
from bs4 import BeautifulSoup

url=urlopen("https://en.wikipedia.org/wiki/Comma-separated_values")
html1=BeautifulSoup(url.read(100000),"lxml")
parse=html1.find_all("table",{"class":"plainlinks metadata ambox ambox-content ambox-Refimprove"})

print(parse)

print(len(parse))
parse



from urllib.request import urlopen
from bs4 import BeautifulSoup

url=urlopen("https://en.wikipedia.org/wiki/Comma-separated_values")
html1=BeautifulSoup(url.read(100000),"lxml")
parse=html1.find_all("table",{"class":"wikitable"})
print(parse)

