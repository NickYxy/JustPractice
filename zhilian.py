import re
import requests
from lxml import etree


job = "通信工程师" #以爬取通信工程师职业为例
leibie = '1'
url_job = []
for page in range(99):
    x = str(page) #爬取的页码
    p = str(page+1)
    print("正在抓取第一"+p+"页...\n") #提示
    url = "http://sou.zhaopin.com/jobs/searchresult.ashx?in=210500%3B160400%3B160000%3B160500%3B160200%3B300100%3B160100%3B160600&jl=上海%2B杭州%2B北京%2B广州%2B深圳&kw="+job+"&p="+x+"&isadv=0" #url地址，此处为示例，可更据实际情况更改
    r = requests.post(url) #发送请求
    data = r.text
    pattern=re.compile('ssidkey=y&amp;ss=201&amp;ff=03" href="(.*?)" target="_blank"',re.S) #正则匹配出招聘信息的URL地址
    tmp_job = re.findall(pattern,data)
    url_job.extend(tmp_job) #加入队列

for x in url_job:
    print(x)
    d = requests.post(x) #发送post请求
    zhiwei = d.text
    selector = etree.HTML(zhiwei) #获得招聘页面源码
    name = selector.xpath('//div[@class="inner-left fl"]/h1/text()') #匹配到的职业名称
    mone = selector.xpath('//div[@class="terminalpage clearfix"]/div[@class="terminalpage-left"]/ul[@class="terminal-ul clearfix"]/li[1]/strong/text()') #匹配到该职位的月薪
    adress = selector.xpath('//div[@class="terminalpage clearfix"]/div[@class="terminalpage-left"]/ul[@class="terminal-ul clearfix"]/li[2]/strong/a/text()') #匹配工作的地址
    exp = selector.xpath('//div[@class="terminalpage clearfix"]/div[@class="terminalpage-left"]/ul[@class="terminal-ul clearfix"]/li[5]/strong/text()') #匹配要求的工作经验
    education = selector.xpath('//div[@class="terminalpage clearfix"]/div[@class="terminalpage-left"]/ul[@class="terminal-ul clearfix"]/li[6]/strong/text()') #匹配最低学历
    zhiweileibie = selector.xpath('//div[@class="terminalpage clearfix"]/div[@class="terminalpage-left"]/ul[@class="terminal-ul clearfix"]/li[8]/strong/a/text()') #匹配职位类别

    match = re.compile('<!-- SWSStringCutStart -->(.*?)<!-- SWSStringCutEnd -->',re.S)#此处为匹配对职位的描述，并且对其结构化处理
    description = re.findall(match,zhiwei)
    des = description[0]
    des = filter_tags(des) #filter_tags此函数下面会讲到
    des = des.strip()
    des = des.replace('&nbsp;','')
    des = des.rstrip('\n')
    des = des.strip(' \t\n')
    try: #尝试判断是否为最后一则
        name = to_str(name[0])
        mone = to_str(mone[0])
        adress = to_str(adress[0])
        exp = to_str(exp[0])
        education = to_str(education[0])
        zhiweileibie = to_str(zhiweileibie[0])
        des = to_str(des)
    except Exception as e:
        continue

def filter_tags(htmlstr):
    #先过滤CDATA
    re_cdata=re.compile('//<!\[CDATA\[[^>]*//\]\]>',re.I) #匹配CDATA
    re_script=re.compile('<\s*script[^>]*>[^<]*<\s*/\s*script\s*>',re.I)#Script
    re_style=re.compile('<\s*style[^>]*>[^<]*<\s*/\s*style\s*>',re.I)#style
    re_br=re.compile('<br\s*?/?>')#处理换行
    re_h=re.compile('</?\w+[^>]*>')#HTML标签
    re_comment=re.compile('<!--[^>]*-->')#HTML注释
    s=re_cdata.sub('',htmlstr)#去掉CDATA
    s=re_script.sub('',s) #去掉SCRIPT
    s=re_style.sub('',s)#去掉style
    #s=re_br.sub('\n',s)#将br转换为换行
    s=re_h.sub('',s) #去掉HTML 标签
    s=re_comment.sub('',s)#去掉HTML注释
    #去掉多余的空行
    blank_line=re.compile('\n+')
    s=blank_line.sub('\n',s)
    # s=replaceCharEntity(s)#替换实体
    return s

conn = pymysql.connect(host='127.0.0.1',user='root',passwd='××××××',db='zhiye_data',port=3306,charset='utf8')
cursor=conn.cursor()

sql='INSERT INTO `main_data_3` (`name`,`mone`,`adress`,`exp`,`education`,`zhiweileibie`,`description`,`leibie`,`company_range`,`company_kind`) VALUES(\''+name+'\',\''+mone+'\',\''+adress+'\',\''+exp+'\',\''+education+'\',\''+zhiweileibie+'\',\''+des+'\',\''+leibie+'\',\'a\',\'b\');'#%(name,mone,adress,exp,education,zhiweileibie,des,leibie)

    #print(sql)
    try:
        cursor.execute(sql)
        conn.commit()
        print (cursor.rowcount)
    except Exception as e:
        print (e)
cursor.close()
conn.close()