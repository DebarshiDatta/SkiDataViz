from bs4 import BeautifulSoup
import requests
import sys
import time


# open file with resorts urls
f = open('resort_urls.txt', 'r')
urls = []

# read in urls
for line in f:
	urls.append(line)

sys.stdout = open('resort_data_test.csv', 'w')

print 'name,vertical,summit,base,lifts,trails,longest_run,snowboarding,terrain_park,half_pipe,annual_snowfall,snowmaking,skiable_area,green,blue,black,double_black,xc,tubing'


# for each state
for i in range(len(urls)):
	# get page
	r = requests.get(urls[i])

	# get text from page object
	data = r.text

	# create soup object
	soup = BeautifulSoup(data)


	table = soup.find_all('table')[6].contents[1]

	data = {}

	data['name'] = (urls[i][urls[i].rfind('/')+1:-6])

	results = table.find_all('td')
	for i in range(len(results)):
		if str(results[i].contents[0])[-1] == ':':
			temp = results[i+1].contents[0]
			if temp.find('.gif') != -1:
				temp = results[i+1].contents[0].contents[0]
			temp = temp.replace(',', '')
			if temp.find('Yes') != -1:
				temp = 1
			elif temp.find('No') != -1:
				temp = 0
			elif temp.find('%') != -1:
				temp = int(temp[:temp.find('%')])
			elif temp.find('feet') != -1:
				temp = int(temp[:temp.find('feet')-1])
			elif temp.find('km') != -1:
				temp = int(temp[:temp.find('km')-1])
			elif temp.find('in') != -1:
				temp = int(temp[:temp.find('in')-1])
			elif temp.find('acre') != -1:
				temp = int(temp[:temp.find('acre')-1])

			data[results[i].contents[0][:-1]] = temp


	sys.stdout.write(data['name'])
	sys.stdout.write(',')

	if 'vertical drop' in data: sys.stdout.write(str(data['vertical drop']))
	sys.stdout.write(',')

	if 'summit' in data: sys.stdout.write(str(data['summit']))
	sys.stdout.write(',')

	if 'base' in data: sys.stdout.write(str(data['base']))
	sys.stdout.write(',')

	if 'lifts' in data: sys.stdout.write(str(data['lifts']))
	sys.stdout.write(',')

	if 'trails' in data: sys.stdout.write(str(data['trails']))
	sys.stdout.write(',')

	if 'longest run' in data: sys.stdout.write(str(data['longest run']))
	sys.stdout.write(',')

	if 'permitted' in data: sys.stdout.write(str(data['permitted']))
	sys.stdout.write(',')

	if 'terrain park' in data: sys.stdout.write(str(data['terrain park']))
	sys.stdout.write(',')

	if 'half-pipe' in data: sys.stdout.write(str(data['half-pipe']))
	sys.stdout.write(',')

	if 'annual snowfall' in data: sys.stdout.write(str(data['annual snowfall']))
	sys.stdout.write(',')

	if 'snowmaking' in data: sys.stdout.write(str(data['snowmaking']))
	sys.stdout.write(',')

	if 'skiable area' in data: sys.stdout.write(str(data['skiable area']))
	sys.stdout.write(',')

	if 'easiest' in data: sys.stdout.write(str(data['easiest']))
	sys.stdout.write(',')

	if 'more difficult' in data: sys.stdout.write(str(data['more difficult']))
	sys.stdout.write(',')

	if 'most difficult' in data: sys.stdout.write(str(data['most difficult']))
	sys.stdout.write(',')

	if 'experts only' in data: sys.stdout.write(str(data['experts only']))
	sys.stdout.write(',')

	if 'x-country' in data: sys.stdout.write(str(data['x-country']))
	sys.stdout.write(',')

	if 'snow tubing' in data: sys.stdout.write(str(data['snow tubing']))
	sys.stdout.write(',')

	sys.stdout.write('\n')

	time.sleep(1)