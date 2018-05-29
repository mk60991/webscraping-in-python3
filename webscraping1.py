# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 10:11:50 2018

@author: hp
"""

from urllib.request  import urlopen
from bs4 import BeautifulSoup

url=urlopen("http://www.citymayors.com/government/us-women-government.html")

set1=BeautifulSoup(url.read(),"lxml")

print(set1)
print(set1.head)
print(set1.table)
print(set1.h2)
print(set1.h4)
print(set1.td)

#

from urllib.request import urlopen
from bs4 import BeautifulSoup

url=urlopen("https://en.wikipedia.org/wiki/Will_Smith")
html1=BeautifulSoup(url.read(),"lxml")

