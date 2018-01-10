#!/usr/bin/env python
#encoding=utf-8
import scrapy
f=open("./debug.txt","w")

class NewsSpider(scrapy.Spider):
	name = "news_spider"
	start_urls= ["http://www.zjhrss.gov.cn/col/col1389524/index.html?uid=4451525&pageNum=1"]

	def parse(self, response):
		print "="*100
		html = response.text
		import re
		for match in re.finditer(r"<a style[\s\S]*?href='(?P<href>[\s\S]*?)'[\s\S]*?>(?P<title>[\s\S]*?)</a>[\s\S]*?>(?P<date>[\s\S]*?)<", html):
        		dict = {}
			dict["title"] = match.group("title")
        		dict["href"] = match.group("href")
        		dict["date"] = match.group("date")
			yield dict
		index = response.url.rfind("=")
		if index > 0:
			a = response.url[:index]
			print "url=>",response.url
			print "index=>",index
			b = int(response.url[index+1:])
			if (b+3) < 723:
				b = b+3
				next_url = a+"="+str(b)
				f.write(next_url+"\r\n")
				f.flush()
				yield response.follow(next_url, self.parse)

