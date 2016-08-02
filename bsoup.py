import urllib
import urllib2
import lxml
from bs4 import BeautifulSoup

#coding:utf-8
import sys 
reload(sys) 
sys.setdefaultencoding("utf-8")

def execute():
    url = "http://www.biquge.la/xiaoshuodaquan/"
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    html = response.read()
    soup = BeautifulSoup(html,"lxml")

    print soup.prettify()
    print soup.title

    #print soup.select('div[class="nav"]')[0].encode("utf-8")
    print soup.select('div[class="novellist"]')[0].encode("utf-8")

if __name__ == '__main__':
    execute()
