# phantomjs download
# pip install selenium

# http://phantomjs.org/download.html
#https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-windows.zip

#after downloading:  Extract into d:/phantomjs Directory

from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver import ActionChains

#driver loading
driver = webdriver.PhantomJS(executable_path='E:/MY DEVELOPING/Scraping/testPhantomjs/bin/Phantomjs')
driver.implicitly_wait(2)
driver.get('http://daum.net/')
driver.get_screenshot_as_file('E:/MY DEVELOPING/Scraping/testPhantomjs/screen.png')
driver.close()
print("saved exactly")