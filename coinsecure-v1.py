import requests
import json
import time as ts
import datetime

print "\n\033[91m Coinsecure INR SELL PRICE \033[0m\n"

while True:
	res = requests.get('https://api.coinsecure.in/v1/exchange/ticker')
	#print(res.text)
	j = json.loads(res.text)
	sell = j['message']['bid']
	buy = j['message']['lastPrice']
	timestamp = int(j['message']['timestamp'])

	date_time = datetime.datetime.now()

	date = date_time.date()  # gives date
	time = date_time.time()  # gives time

	print "Time:"+str(time.hour)+":"+str(time.minute)+", BTC PRICE: \x1b[6;30;42m"+str(sell)[0:6]+"\x1b[0m INR "
	ts.sleep(61)
