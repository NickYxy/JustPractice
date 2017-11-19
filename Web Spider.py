# This is the practice on the web crawling book

from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
import re
import pymysql.cursors
import random
import datetime

#用系统当前时间生成一个随机数生成器，这样可以保证在每次程序运行的时候，维基百科词条的选择都是一条全新的随机路径
# random.seed(datetime.datetime.now())
#
#
# def get_links(article_url):
#     html = urlopen("https://en.wikipedia.org/" + article_url)
#     bs = BeautifulSoup(html, "html.parser")
#
#     return bs.find("div", {"id": "bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))
#
# links = get_links("wiki/Kevin_Bacon")
#
# while len(links) > 0:
#     newArticle = links[random.randint(0, len(links)-1)].attrs["href"]
#     print(newArticle)
#     links = get_links(newArticle)

# for link in bs.find("div", {"id": "bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$")):
#     if "href" in link.attrs:
#         print(link.attrs['href'])


#链接去重

# pages = set()
#
#
# def getlinks(pageurl):
#     global pages
#     html1 = urlopen("https://en.wikipedia.org"+pageurl)
#     bs4 = BeautifulSoup(html1, "html.parser")
#     for link in bs4.findAll("a", href=re.compile("^(/wiki/)")):
#         if "href" in link.attrs:
#             if link.attrs['href'] not in pages:
#                 #我们遇到了新页面
#                 newPage = link.attrs['href']
#                 print(newPage)
#                 pages.add(newPage)
#                 getlinks(newPage)
#
# getlinks("")


#采集数据

# pages = set()
# def getlinks(pageurl):
#     global pages
#     html = urlopen("https://en.wikipedia.org"+pageurl)
#     bs4 = BeautifulSoup(html, 'html.parser')
#     try:
#         print(bs4.h1.get_text())
#         print(bs4.find(id="mw-content-text").findAll("p")[0])
#         print(bs4.find(id="ca-edit").find("span").attrs['href'])
#     except AttributeError:
#         print("页面缺少一些属性！")
#
#     for link in bs4.findAll("a", href=re.compile("^(/wiki/)")):
#         if 'href' in link.attrs:
#             if link.attrs['href'] not in pages:
#                 newpage = link.attrs['href']
#                 print("----------------\n"+newpage)
#                 pages.add(newpage)
#                 getlinks(newpage)
#
# getlinks("")


#高级网络数据采集

# def ngrams(input1, n):
#     input1 = re.sub('\n+', " ", input1)
#     input1 = re.sub(' +', " ", input1)
#     input1 = bytes(content, "UTF-8")
#     # input1 = input1.decode("ascii", "ignore")
#     input1 = input1.split(" ")
#     output = []
#     for i in range(len(input1)-n+1):
#         output.append(input1[i:i+n])
#     return output
#
# html = urlopen("https://en.wikipedia.org/wiki/Python")
# bs4 = BeautifulSoup(html, 'html.parser')
# content = bs4.find("div", {"id": "mw-content-text"}).get_text()
# ngram = ngrams(content, 2)
# print(ngram)
# print("2-ngrams count is: " + str(len(ngram)))


#提交表单
params = {'firstname': 'Ryan', 'lastname': 'Mitchell'}
r = requests.post("http://pythonscraping.com/files/processing.php", data=params)
print(r.text())