#!/usr/bin/python3
import requests
import logging
import time

logging.basicConfig(filename='ddns.log', level=logging.DEBUG, filemode='a', format='%(asctime)s - %(message)s')

username = 'username'
password = 'password'
hostname = 'your-domain.com'
url = 'https://' + username + ':' + password + '@domains.google.com/nic/update?hostname=' + hostname

while True:
	response = requests.post(url)
	output = response.content.decode('utf-8')
	logging.debug('Response from DDNS update: '+ output)
	time.sleep(300)
