#!/usr/bin/python
import requests
import logging
import time
from urllib2 import urlopen

logging.basicConfig(filename='ddns.log', level=logging.DEBUG, filemode='a', format='%(asctime)s - %(message)s')

username = 'username'
password = 'password'
hostname = 'your-domain.com'
old_ip = ''

while True:
	my_ip = urlopen('https://domains.google.com/checkip').read() 
	if my_ip != old_ip:
		url = 'https://' + username + ':' + password + '@domains.google.com/nic/update?hostname=' + hostname
			response = requests.post(url)
			output = response.content.decode('utf-8')
			if 'good' in output:
				old_ip = my_ip
			logging.debug('Response from DDNS update: '+ output)
	time.sleep(10)
