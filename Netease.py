# from bs4 import BeautifulSoup
# import urllib.request
# import socket
import requests

# passing parameters to URL
# payload = {'key1': 'value1', 'key2': 'value2'}
# r = requests.get("http://www.163.com", params=payload)
# print(r.url)

#response content
# r = requests.get("http://api.github.com")
# print(r.text)
# with open(filename, 'wb') as fd:
#     for chunk in r.iter_content(chunk_size=128):
#         fd.write(chunk)
#
from urllib.request import urlopen, HTTPError
from bs4 import BeautifulSoup

def get_url(url):
    try:
        html = urlopen("http://www.baidu.com")
    except HTTPError as e:
        print(e)
        return None
    try:
        bsObj = BeautifulSoup(html.read)
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title

title = get_url("http://www.baidu.com")
if title == None:
    print("Page not found")
else:
    print(title)

html = urlopen("http://www.baidu.com")
bs = BeautifulSoup(html.read)
namelist = bs.findAll("span", {"class":{"green", "red"}}, text="the prince", id="text")
for name in namelist:
    print(name.get_text())
for child in bs.find("table").children:
    print(child)


for child in bs.find("table").tr.next_siblings:
    print(child)

















# import requests
#
#
# request = requests.get("http://weibo.com/", auth = ('bing900713@sina.com', 'wo3'))
# print(request.status_code)
# print(request.headers['content-type'])
# print(request.encoding)



#
# class sohuSpider(object):
#     def __init__(self, url):
#         self.url = url
#
#     def getNextUrls(self):
#         urls = []
#         request = urllib.request.urlopen(self.url)
#         request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; \
#             WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36')
#
#         try:
#             html = urllib.request.urlopen(request)
#         except socket.timeout as e:
#             pass
#         except urllib.request.URLError as ee:
#             pass
#
#         soup = BeautifulSoup(html, 'html.parser')
#         for link in soup.find_all('a'):
#             print("http://m.sohu.com" + link.get('href'))
#             if link.get('href')[0] == '/':
#                 urls.append("http://m.sohu.com" + link.get('href'))
#         return urls
#
#
# def getNews(url):
#     print(url)
#     xinwen = ''
#     request = urllib.request.urlopen(url)
#     request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; \
#                 WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36')
#
#     try:
#         html = urllib.request.urlopen(request)
#     except urllib.request.URLError as ee:
#         pass
#
#     soup = BeautifulSoup(html, 'html.parser')
#     for news in soup.select('p.para'):
#         xinwen += news.get_text().decode('utf-8')
#     return xinwen
#
#
# class News(object):
#     """
#      source:from where 从哪里爬取的网站
#      title:title of news  文章的标题
#      time:published time of news 文章发布时间
#      content:content of news 文章内容
#      type:type of news    文章类型
#
#     """
#     def __init__(self, source, title, time, content, type):
#         self.source = source
#         self.title = title
#         self.time = time
#         self.content = content
#         self.type = type
#
#     file = open('/Users/nickyuan/Documents/Python Practice/sohu.txt', 'a')
#     for i in range(38, 50):
#         for j in range(1, 5):
#             url = "http://m.sohu.com/cr" + str(i) + "/?page=" + str(j)
#             print(url)
#             s = sohuSpider(url)
#             for newsUrl in s.getNextUrls():
#                 file.write(getNews(newsUrl))
#                 file.write('\n')
#                 print("--------------------------------")
