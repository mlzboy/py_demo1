#!/usr/bin/env python
#encoding=utf-8
import urllib2
import codecs
url = "http://www.zjhrss.gov.cn/col/col1389524/index.html"
html = urllib2.urlopen(url).read()
f = codecs.open("./html.txt","w","utf-8")
print "html type is:",type(html)
f.write(html.decode("utf-8","ignore"))
f.close()
from pyquery import PyQuery as pq
from lxml import etree
#d = pq(etree.fromstring(html))
print "html type:",type(html)
d = pq(html)
d = d("#4451525").text()
print "d type:",type(d)
d = pq(d)
for elem in d("record"):
	print elem


