#!/usr/bin/env python
#encoding=utf-8
import urllib2
import codecs
import re
#下载
url = "http://www.zjhrss.gov.cn/col/col1389524/index.html"
html = urllib2.urlopen(url).read()
#抽取
for match in re.finditer(r"<a style[\s\S]*?href='(?P<href>[\s\S]*?)'[\s\S]*?>(?P<title>[\s\S]*?)</a>[\s\S]*?>(?P<date>[\s\S]*?)<", html):
        title = match.group("title")
        href = match.group("href")
        date = match.group("date")
	#输出、存储
	print title,href,date

