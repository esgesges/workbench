
import json
import requests
import os
from datetime import datetime, timedelta


def req(url):
	response = requests.get(url)
	jresponse = response.json()
	return jresponse


def catch_data(response):
	repeat = False
	full = ""
	done = True

	with open("assetID.txt", "r+") as fid:
		assetID = response['pageProps']['dehydratedState']['queries'][0]['state']['data']['data']['_assetId']
		id = fid.read()
		if id != assetID:
			fid.write(str(assetID))
			for stato in response['pageProps']['dehydratedState']['queries'][0]['state']['data']['data']:


				if not repeat:
					issuerName = stato['issuer']['issuerName']
					issuerTicker = stato['issuer']['issuerTicker']
					name_str = stato['politician']['lastName']
					repGap_str = stato['reportingGap']
					pubDate_str = stato['pubDate']

					if stato['reportingGap'] < 120 and stato['txType'] == "buy":
						print(issuerName)
						print(issuerTicker)
						print(name_str)
						print(repGap_str)
						print("\n\n")
						full = full + "\n\n" + issuerName + "\n" + str(issuerTicker) + "\n" + name_str + "\n" + str(pubDate_str)
		if id == assetID:
			repeat = True

	if repeat:
		full = ""
	return full


def bot_sendMSG(message):
	url = "https://api.telegram.org/bot7090375373:AAHNBHKUGn4Odg5FYJb30nQoK63TJW4dw0E/sendMessage"

	querystring = {"chat_id":"716727488","text":message}
	headers = {"Authorization": "Bearer 7090375373:AAHNBHKUGn4Odg5FYJb30nQoK63TJW4dw0E"}
	response = requests.request("GET", url, headers=headers, params=querystring)

	print(response.text)




def confronta_date(response):
	for stato in response['pageProps']['dehydratedState']['queries'][0]['state']['data']['data']:

		pubDate_str = stato['pubDate']
		filingDate_str = stato['txDate']
		asset_str = stato['asset']
		name_str = stato['politician']['lastName']

		pubDate = datetime.strptime(pubDate_str, '%Y-%m-%dT%H:%M:%SZ')
		pubdate_ymd = pubDate.strftime('%Y-%m-%d')
		filingdate = datetime.strptime(filingDate_str, '%Y-%m-%d')
		print(pubdate_ymd)
		print(filingdate)
		if pubDate - filingdate < timedelta(days=60):
			print("\n\n\n")
			print(pubDate-filingdate)
			print(stato['reportingGap'])
			print("\n\n" + pubdate_ymd)
			print(filingdate)
			print(asset_str)
			print(name_str)
def main():
	url = "https://www.capitoltrades.com/_next/data/hQiDrmIu3vjPhnfmY_lh8/trades.json"
	response = req(url)
#	confronta_date(response)
	result = catch_data(response)
	bot_sendMSG(result)

main()
