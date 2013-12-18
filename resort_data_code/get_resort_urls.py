from bs4 import BeautifulSoup
import requests

# open state urls list
f = open('state_urls.txt', 'r')
urls = []

for line in f:
	urls.append(line)

resorts = []

# for each state
for url in urls:
	# get page
	r = requests.get(url)

	# get text from page object
	data = r.text

	# create soup object
	soup = BeautifulSoup(data)

	# flag tells you if you are resort links yet
	flag = 0
	# front of the urls
	front = 'http://www.skiresortsnow.com'

	# for each link in the page
	for link in soup.find_all('a'):
		# if you are past the resort links
		if link.get('href') == '/ski-resorts/usa/alaska/':
			# leave loop
			break	
		# if you are at the resorts
		elif flag:
			# add to the list or resort urls
			resorts.append(front + link.get('href'))
		# if at the last link before resort urls set flag
		elif link.get('href') == 'http://www.abc.net.au/melbourne/news/200310/s961541.htm':
			flag = 1


# open new file
g = open('resort_urls.txt', 'w')

# add all the resorts to file
for resort in resorts:
	g.write(resort + '\n')


g.close()
