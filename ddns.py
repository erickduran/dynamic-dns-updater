#!/usr/bin/python3
import requests
import logging
import time
from urllib.request import urlopen

logging.basicConfig(filename='ddns.log', level=logging.DEBUG, filemode='a', format='%(asctime)s - %(message)s')

username = 'username'
password = 'password'
hostname = 'example.com'
old_ip = ''

while True:
	try:
		my_ip = urlopen('https://domains.google.com/checkip').read() 
	except:
		logging.debug('CATCHED AN ERROR... RETRYING IN 10 SECONDS')
		time.sleep(10)
	else:
		if my_ip != old_ip:
			url = 'https://{}:{}@domains.google.com/nic/update?hostname={}'.format(username, password, hostname)
			response = requests.post(url)
			output = response.content.decode('utf-8')
			if 'good' in output or 'nochg' in output:
				old_ip = my_ip
			logging.debug('-- OUTPUT FOR UPDATE: '+ hostname +' --')
			logging.debug('Response from DDNS update: '+ output)
		time.sleep(10)
