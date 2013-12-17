from bs4 import BeautifulSoup
import requests

# open file with resorts urls
f = open('resort_urls.txt', 'r')
urls = []

# read in urls
for line in f:
	urls.append(line)



