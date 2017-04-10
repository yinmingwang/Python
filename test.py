import urllib.request
import re
"""req=urllib.request.urlopen('http://www.imooc.com/course/list')
buf=req.read()
buf=buf.decode('UTF-8')
listurl=re.findall(r'src=.+\.jpg',buf)
listurl=re.findall(r'http:.+\.jpg',buf)#显示图片的网址
listurl
#将图片写入本地
i=0
for url in listurl:
     f=open(r"D:\pic"+'/'+str(i)+'.jpg','wb')
     req=urllib.request.urlopen(url)
     buf=req.read()
     f.write(buf)
     i+=1"""

from urllib import request
captcha_url = 'http://hire.jobcn.com/randomCode.xhtml'
for k in range(1,20000):
    request.urlretrieve(captcha_url,'C:\\Users\\yinmw\\Desktop\\picture\\%d.jpg'%k)


#f = open('C:\\Users\\yinmw\\Desktop\\pic\\%s.jpg' % x, 'wb')
#f.write(im_data)
#关闭文件#
#f.close()