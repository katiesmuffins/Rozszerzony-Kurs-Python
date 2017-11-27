#!/usr/bin/env python3
# coding: utf8 

import re
import urllib.request
from bs4 import BeautifulSoup
from functools import reduce
import timeit

def searching(url, depth):
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    action(url)
    if depth>0:
        links = soup.findAll('a')
        list_of_links = [link['href'] for link in links]
        list_of_links = list(filter(lambda x: re.match("(http://.*)", x), list_of_links))
        for link in list_of_links:
            print(link)
            try: 
                searching(link, depth-1)
            except: 
                print("Cannot open a site")


def action(url):
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    print (soup.body.findAll(text=re.compile('Python')))


if __name__ == '__main__':
    print(searching('http://www.ii.uni.wroc.pl/~marcinm/dyd/python/' , 1))
    #print(timeit.timeit("searching('http://www.ii.uni.wroc.pl/~marcinm/dyd/python/' , 1), ", setup="from __main__ import searching", number=1))
