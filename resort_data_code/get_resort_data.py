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

# open file for output of data
sys.stdout = open('../Data/resort_data.csv', 'w')

# first line of the file for labeling purposes
print 'name,state,vertical,summit,base,lifts,trails,longest_run,snowboarding,terrain_park,half_pipe,annual_snowfall,snowmaking,skiable_area,green,blue,black,double_black,xc,tubing'


# for each state
for i in range(len(urls)):
	# get page
	r = requests.get(urls[i])

	# get text from page object
	data = r.text

	# create soup object
	soup = BeautifulSoup(data)

	# get the table that has the relevant data
	table = soup.find_all('table')[6].contents[1]

	# create an empty dictionary for the data
	data = {}

	# add the resort name
	n = urls[i].rfind('/')
	data['name'] = urls[i][n+1:-6]
	# add the state
	m = urls[i].rfind('/',0,n)
	data['state'] = urls[i][m+1:n]

	# find the td tags in the table
	results = table.find_all('td')
	for i in range(len(results)):
		# if the tag contains on of the labels then set it up in the dictionary
		if str(results[i].contents[0])[-1] == ':':
			temp = results[i+1].contents[0]
			# if one of the percentages get tag within tag
			if temp.find('.gif') != -1:
				temp = results[i+1].contents[0].contents[0]
			# remove commas
			temp = temp.replace(',', '')
			# if yes change to 1
			if temp.find('Yes') != -1:
				temp = 1
			# if no change to 0
			elif temp.find('No') != -1:
				temp = 0
			# edit for removing labels
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

			# add to dictionary
			data[results[i].contents[0][:-1]] = temp


	# output all values that exist for this resort

	sys.stdout.write(data['name'])
	sys.stdout.write(',')

	sys.stdout.write(data['state'])
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

	# sleep to avoid DDOS
	time.sleep(1)