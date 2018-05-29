# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 15:13:39 2018

@author: hp
"""

import urllib.request as url12

url=("https://www.icc-cricket.com/rankings/mens/team-rankings/odi")

page=url12.urlopen(url)

from bs4 import BeautifulSoup

soup1=BeautifulSoup(page,"lxml")
all_tables=soup1.find_all("table")

right_table=soup1.find("table", class_="table")

A=[]
B=[]
C=[]
D=[]
E=[]

for row in right_table.findAll("tr"):
    cells=row.findAll('td')    
    if len(cells)==5:
        A.append(cells[0].find(text=True))
        B.append(cells[1].text.strip())
        C.append(cells[2].find(text=True))
        D.append(cells[3].find(text=True))
        E.append(cells[4].find(text=True))
       # F.append(cells[4]).find(text=True))
        #G.append(cells[5]).find(text=True))
    
    
    
import pandas as pd
df1=pd.DataFrame(A,columns=["Pos"])
df1["Team"]=B
df1["Matches"]=C
df1["Points"]=D
df1["Rating"]=E











