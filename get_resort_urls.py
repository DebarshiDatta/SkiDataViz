from bs4 import BeautifulSoup
import requests


f = open('state_urls.txt', 'r')
urls = []

for line in f:
	urls.append(line)

resorts = []

for url in urls:
	r = requests.get(url)

	data = r.text

	soup = BeautifulSoup(data)

	flag = 0
	front = 'http://www.skiresortsnow.com'

	for link in soup.find_all('a'):
		if link.get('href') == '/ski-resorts/usa/alaska/':
			break	
		elif flag:
			resorts.append(front + link.get('href'))
		elif link.get('href') == 'http://www.abc.net.au/melbourne/news/200310/s961541.htm':
			flag = 1


g = open('resort_urls.txt', 'w')

for resort in resorts:
	g.write(resort + '\n')


g.close()
