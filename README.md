# dynamic-dns-updater
## What it is?
A simple Python script to update your Dynamic DNS records on Google Domains. You can read more about it [here](https://blog.erickduran.com/programming/2019/02/09/ddns-python-script/).


## Prerequisites
- Python (tested on 2.7)
- A Google Domains domain

## Setting up Google Domains
The first step to take is setting up the Dynamic DNS synthetic record that will point to your server. If you don't know how to do this, please make sure you have followed all steps from 1 to 11 from [this page](https://support.google.com/domains/answer/6147083?hl=en).

## Setting up the script
You should configure the following variables (all obtained from your Google Domains DNS page):
- `username` 
- `password`
- `hostname`

You can also configure the line `time.sleep(10)` to a shorter or longer timespan (in seconds). 

The script includes a few logging lines to keep track of all the requests-responses. This will be stored automatically in a file called `ddns.log`. Feel free to comment this out if you don't need it.

## Running the script

To test the script, just `cd` to the directory where you stored the script and run the following command:
```bash
python ddns.py
```
Wait for the time you specified and check in your Google Domains page that the IP has changed to your current server's public IP address. 

