# bringing the lists of book from wikipedia
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
#pip install regex

html = urlopen('http://en.wikipedia.org/wiki/Kevin_Bacon')
bs = BeautifulSoup(html,'html.parser')
for link in bs.find_all('a'):
	if 'href' in link.attrs:
		print(link.attrs['href'])


html = urlopen('http://en.wikipedia.org/wiki/Kevin_Bacon')
bsone = BeautifulSoup(html,'html.parser')

links = bsone.find('div',{'id':'bodyContent'}).find_all('a', href = re.compile('^(/wiki/)((?!:).)*$'))
print("link count:",len(links))
for link in links:
	if 'href' in link.attrs:
		print(link.attr['href'])