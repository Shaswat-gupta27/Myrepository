# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 22:20:28 2020

@author: Shashwat
"""

import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.downloader.download('vader_lexicon')
sid=SentimentIntensityAnalyzer()
dfs=['I will kill the person','Set your goals right','I am proud of my country','I am in love']
for data in dfs:
    ss=sid.polarity_scores(data)
    print(data)
    print(ss)
    '''for k in ss:
        print(k,ss[k])
    if ss['compound'] >0:
        print("Positive Statement!")
    elif ss['compound']==0:
        print("Neutral Statement!")
    else:
        print("Negative statement!")'''
