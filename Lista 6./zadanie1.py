#!/usr/bin/env python3
# coding: utf8 

import argparse
import re
import urllib.request
from bs4 import BeautifulSoup
from functools import reduce
from multiprocessing import Pool
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
    parser = argparse.ArgumentParser()
    parser.add_argument("url", type=str, help="the URL of page, which we start searching")
    parser.add_argument("depth", type=int, help="the depth of searching")
    args = parser.parse_args()
    if args.url and args.depth:
        pool = Pool(processes=20)
        res = pool.apply_async(searching, (args.url,args.depth,))      # runs in *only* one process
        print (res.get(timeout=None))
        #print(timeit.timeit("res", setup="from __main__ import res"))
        #print(searching('http://www.ii.uni.wroc.pl/~marcinm/dyd/python/' , 1))
        #print(timeit.timeit("searching('http://www.ii.uni.wroc.pl/~marcinm/dyd/python/' , 1)", setup="from __main__ import searching()"))
        
#wywolanie w terminalu: python3 zadanie1.py http://www.ii.uni.wroc.pl/~marcinm/dyd/python/ 1