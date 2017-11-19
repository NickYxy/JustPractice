__author__ = 'nickyuan'
from bs4 import BeautifulSoup
from urllib import parse
import requests
import csv

headers = {
    'Accept': '*/*',
    'Host': 'bj.lianjia.com',
    'Referer': 'https://bj.lianjia.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
}

url = 'https://bj.lianjia.com/zufang/haidian'

if __name__ == '__main__':
    start_page = 1
    end_page = 100
    price = 7
    with open('/Users/nickyuan/Downloads/爬虫/链家/haidian.csv', 'wb') as f:
        print('start............')
        while start_page <= end_page:
            start_page += 1
            print('get:{}'.format(url.format(page=start_page, price=price)))
            s = requests.session()
            s = BeautifulSoup(s.get(url=url, headers=headers).content, "html.parser")
            house_list = s.select('.main-box clear > .con-box > .list-wrap')

            if not house_list:
                break
            for house in house_list:
                house_title = house.select('.col-1 > .where > span').string.encode('utf-8')
                house_addr = house.select('.other > .con > a')[0].string.encode('utf-8')
                house_price = house.select('.col-3 > .price > .num')[0].string.encode('utf-8')
                csv_writer = csv.writer(f)
                csv_writer.writerow([house_title, house_addr, house_price])
        print('end...............')
