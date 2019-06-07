import urllib.parse
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.kyobobook.co.kr/search/SearchKorbookMain.jsp?vPstrCategory=KOR&vPstrKeyWord=java&vPplace=top")
bsObj = BeautifulSoup(html,"html.parser")

# first: #container > div:nth-child(22) > form > table > tbody > tr:nth-child(4) > td.detail > div.title > a > strong
titles = bsObj.select("td.detail > div.title > a > strong")

print(len(titles),"books found.")
print("======================")
for title in titles:
	print(title.string.strip())