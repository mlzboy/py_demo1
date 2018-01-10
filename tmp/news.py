# -*- coding: utf-8 -*-
import scrapy


class NewsSpider(scrapy.Spider):
    name = 'news'
    allowed_domains = ['http://www.zjhrss.gov.cn/col/col1389524/index.html']
    start_urls = ['http://http://www.zjhrss.gov.cn/col/col1389524/index.html/']

    def parse(self, response):
	html = response.text #urllib2.urlopen(url).read()
	import re
	title = "t1"
	href = "h1"
	date = "d1"
	print title,href,date
        yield {"title":title,"href":href,"date":date}
        yield {"title":title,"href":href,"date":date}
        yield {"title":title,"href":href,"date":date}
        yield {"title":title,"href":href,"date":date}

