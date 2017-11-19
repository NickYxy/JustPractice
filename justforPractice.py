# __author__ = 'nickyuan'
#
# import requests
# from bs4 import BeautifulSoup
#
# headers = {
#     'Accept': '*/*',
#     'Host': 'music.163.com',
#     'Referer': 'https://music.163.com/',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
# }
#
# url = 'https://music.163.com/playlist?id=41066177'
#
# #753100396#14291453#494820921#41647616#45448579#60555476#41066177
#
# s = requests.session()
# s = BeautifulSoup(s.get(url=url, headers=headers).content, "html.parser")
# main = s.find('ul', {'class': 'f-hide'})
#
#
#     # print('{} : {}'.format(music.text, music['href'])).encode('utf-8'
# with open('/Users/nickyuan/Downloads/netease.txt', 'wb') as f:
#     for music in main.find_all('a'):
#         f.write(('{} : {}'.format(music.text, music['href'])).encode('utf-8'))
#         f.write(('\n').encode('utf-8'))

# ------------------------------------------------------------------------------------------
# print(dir('string'))
# def cap_string(str):
#     s = str.split(' ')
#     s2 = []
#     for s1 in s:
#         s2.append(s1.capitalize())
#     print(s2)
#     return ' '.join(s2)

# def cap_string(str):
#     return ' '.join([i.title() for i in str.split(' ')])
#
#
# str = 'i love you so much darling, will you be my valentine'
# print(cap_string(str))

# ------------------------------------------------------------------------------------------

# def letter_count(str):
#     return [(s, str.count(s)) for s in set(str)]
#
#
#
# str = 'i love you so much darling, will you be my valentine'
# print(letter_count(str))
# print(set(str))

from flake8.main import git

# a = [1, 2, 3, 4]
# print(a[2:])
# print(a[-2:])
# print(a[10:])
# print(a[::-1])
# print(a[:])
# print(id(a[:]) == id(a))

# print([x**2 for x in range(10)])
# x = 0.5
# while x!= 1.0:
#     print(x)
#     x += 0.1

for b in (a for a in range(10)):
    print(b)
