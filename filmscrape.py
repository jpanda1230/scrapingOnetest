
import urllib.parse
from urllib.request import urlopen
from bs4 import BeautifulSoup

file = open('E:/MY DEVELOPING/Scraping/testPhantomjs/filmname.txt', 'w', encoding='utf-8')

review_list = []

for n in range(1, 11): # 1~11page collecting
    url = 'http://movie.daum.net/moviedb/grade?movieId=108880&type=netizen&page={0}'
format(n)
webpage = urlopen(url)
source = BeautifulSoup(webpage, 'html.parser', from_encoding='utf-8')
reviews = source.select(\
    '#mArticle > div.detail_movie.detail_rating > div.movie_detail > div.main_detail > ul > li > div > p')

for review in reviews:
	str = review.get_text().strip()
	print(str)
	review_list.append(str)

#store into file

for review in review_list:
	file.write(review+'\n')
file.close