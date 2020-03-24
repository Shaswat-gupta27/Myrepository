# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 11:51:42 2019

@author: Shashwat
"""


from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "http://yellowpages.indiaetrade.com/alphabetical_listing/okhla_industrial_area.html"
products=[] #List to store name of the product
prices=[] #List to store price of the product
page = BeautifulSoup(requests.get(url).text, "lxml")
for a in page.findAll('span',class_='company'):
    print(a.text)