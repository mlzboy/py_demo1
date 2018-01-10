#!/usr/bin/env python
#encoding=utf-8
from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import codecs
display = Display(visible=0, size=(800, 600))
display.start()
f = codecs.open("./rendered_html.txt","w","utf-8")
#chrome_options = webdriver.ChromeOptions()
chrome_options = Options()
# 使用headless无界面浏览器模式
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.binary_location = "/usr/bin/chromium-browser"
# 启动浏览器，获取网页源代码
browser = webdriver.Chrome(executable_path="/usr/local/chromedriver-Linux64",chrome_options = chrome_options)
mainUrl = "http://www.zjhrss.gov.cn/col/col1389524/index.html?uid=4451525&pageNum=1"
browser.get(mainUrl)
#print(browser.page_source)
f.write(browser.page_source)
f.close()
import time
time.sleep(5)
browser.quit()
