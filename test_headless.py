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

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
desired = DesiredCapabilities.CHROME
desired ['loggingPrefs'] = { 'browser':'ALL' }
import codecs
#display = Display(visible=0, size=(800, 600))
#display.start()
f = codecs.open("./rendered_html.txt","w","utf-8")
#chrome_options = webdriver.ChromeOptions()
chrome_options = Options()
# 使用headless无界面浏览器模式
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.binary_location = "/usr/bin/chromium-browser"
# 启动浏览器，获取网页源代码
browser = webdriver.Chrome(executable_path="/usr/local/chromedriver-Linux64",chrome_options = chrome_options,desired_capabilities=desired)
mainUrl = "http://www.zjhrss.gov.cn/col/col1389524/index.html?uid=4451525&pageNum=1"
browser.get(mainUrl)
#print(browser.page_source)
f.write(browser.page_source)
f.close()
import time
time.sleep(2)
print "zz"*10
f2 = codecs.open("./2.html","w","utf-8")
browser.execute_script("$('a.default_pgBtn')[2].click();")
browser.execute_script("console.log('hahaha');")
browser.execute_script("console.log('hahaha2');")
f2.write(browser.page_source)
f2.close()
print browser.get_log("browser")
#embedded jquery
#https://www.cnblogs.com/shizioo/p/3813929.html
#browser.quit()
#cookie add
#https://www.cnblogs.com/zhao-ying-jie/p/7084636.html
