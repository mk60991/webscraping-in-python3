# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 12:22:43 2018

@author: hp
"""

#exception handling in webscaraping
from urllib.request import urlopen
from bs4 import BeautifulSoup

from urllib.error import HTTPError
def getTitle(url):
    try:
        html=urlopen(url)
    except HTTPError as e:
        #print("httperror found while opening url")
        return None
    
    try:
        page=BeautifulSoup(html.read(90824),"lxml")
        title=page.body.h1.text
    except AttributeError as e:
        return None
       # print("attribute error while reading page")
        
    return title
    
title=getTitle("https://en.wikipedia.org/wiki/Comma-separated_values")

if title==None:
    print("title not found")
else:
    print(title)
    
    
    
    
    # 2nd method without return sataement
    
    
    
    
    
from urllib.request import urlopen
from bs4 import BeautifulSoup

from urllib.error import HTTPError
def getTitle(url):
    try:
        html=urlopen(url)
    except HTTPError as e:
        print("httperror found while opening url")
        
    
    try:
        page=BeautifulSoup(html.read(90824),"lxml")
        title=page.body.h1.text
    except AttributeError as e:
        print("attribute error while reading page")
        
    return title
    
title=getTitle("https://en.wikipedia.org/wiki/Comma-separated_values")
print(title)
