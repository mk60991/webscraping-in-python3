# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 11:27:57 2018

@author: hp
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup

url=urlopen("https://en.wikipedia.org/wiki/Comma-separated_values")
html1=BeautifulSoup(url.read(),"lxml")

print(html1.head)

print(html1.title)

print(html1.div)


print(html1.table)

print(html1.table.title)
print(html1.table.td)

print(html1.body)
print(html1.body.h1)

print(html1.body.ul)
print(html1.body.ul.li)
print(html1.body.ul.li.a)
print(html1.body.ul.li.a.span)

#dir is the helping table of beautifulsoup which is used to list function used in beaytifulsoup
dir(html1)

#used of beautifulsoup function
print(html1.len)


print(html1.gettext)

print(html1.text)

print(html1.body.text)

print(html1.head.text)
print(html1.head.get_attribute_list)

#it give rough format
print(html1.p)
print(html1.p.sizeof)
print(html1.p.a)
print(html1.p.a.title)

#by using function "text" it give clear format of that rough text
print(html1.p.text)
print(html1.p.a.title.text)

#in clear format
print(html1.body.text)