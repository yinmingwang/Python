# coding:utf-8
import requests
from lxml import html
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
k = 1
for j in range(10):
    url = 'https://movie.douban.com/top250?start={}&filter='.format(j*25)
    con = requests.get(url).content
    sel=html.fromstring(con)
    infomation = sel.xpath('//div[@class = "info"]')
    for i in infomation:
        title = i.xpath('div[@class="hd"]/a/span[@class="title"]/text() ')[0]
        info = i.xpath('div[@class="bd"]/p[1]/text()')
        # print info[0]
        info_1 = info[0].replace(" ", "").replace("\n", "")
        data = info[1].replace(" ", "").replace("\n", "").split("/")[0]
        country = info[1].replace(" ", "").replace("\n", "").split("/")[1]
        geners = info[1].replace(" ", "").replace("\n", "").split("/")[2]
        rate = i.xpath('div[@class="bd"]/div[@class="star"]/span[@class="rating_num"]/text()')[0]
        comcount = i.xpath('//div[@class="star"]/span[4]/text()')[0]
        with open("top250.txt", "a") as f:
            f.write( "TOP%s\n影片名称：%s\n评分：%s %s\n上映日期：%s\n上映国家：%s\n%s\n" % (k, title, rate, comcount,data,country,info_1) )
            f.write("================================================================\n")
            k += 1
