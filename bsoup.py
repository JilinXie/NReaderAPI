# -*- coding: utf-8 -*-

import urllib
import urllib2
import lxml
from bs4 import BeautifulSoup
import requests
import sys
def execute():

    baseurl = "http://www.biquge.la/xiaoshuodaquan/"
    noveinfo = {}
    result = requests.get(baseurl)
    result.encoding = 'GBK'
    print result.status_code
    #print result.url
    #print result.text

    soup = BeautifulSoup(result.text,"lxml")

    print soup.prettify()
    print soup.title

    print soup.select('div[class="novellist"]')[0].encode("utf-8")

if __name__ == '__main__':
    execute()

