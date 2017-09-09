#!/usr/bin/python
import requests
from lxml import html

def generateUrls():
	baseURL = 'URL REMOVED'
	url = []
	# Iterate through range of lowercase ASCII letters
	for i in range(97,123):
		url.append(baseURL + chr(i))
	return url

def writeToFile(wordlist):
	file = open("BasqueWordlist1.txt", "w")
	for word in wordlist:
		file.write(word + '\n')
	file.close()

if __name__ == '__main__':
	urlList = generateUrls()
	wordlist = []

	for url in urlList:
		page = requests.get(url)
		tree = html.fromstring(page.content)
		# Get the wordlist for current letter of the alphabet
		temp_wordlist = tree.xpath('//*[@id="bas"]/a/text()')
		# Add the wordlist from the current letter onto the master wordlist
		wordlist.extend(temp_wordlist)

	writeToFile(wordlist)
