import urllib2
from bs4 import BeautifulSoup
from nltk.corpus import cmudict
import nltk
import string
import numpy as np
from bld_sentence import build_sentence

ph = cmudict.dict()

word_alerts = ["stars", "exoplanets", "Marcy"]

soup = BeautifulSoup(urllib2.urlopen("http://arxiv.org/list/astro-ph/new").read())
# print soup.find_all('Comment')

def find_alerts(soup):
    alerts = []
    for row in soup:
        st = str(row)
        print st
        sentence = nltk.word_tokenize(st)
        for full_word in sentence:
            word = full_word.split("-")
            for w in word:
                for alert in word_alerts:
                    if alert == word[0]:
                        print "ALERT!", word[0]
                        alerts.append(st)
#     for i in alerts:
#         print i
#         raw_input("enter")
    return alerts
#
find_alerts(soup)

print soup('dd', {'class': 'descriptor'})
print soup('div', {'class': 'descriptor'})
#
# for row in soup('table', {'class': 'spad'})[0].tbody('tr'):
#     tds = row('td')
#     print tds[0].string, tds[1].string
#     raw_input("enter")
