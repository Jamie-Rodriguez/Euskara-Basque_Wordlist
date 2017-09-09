#!/usr/bin/python
from bs4 import BeautifulSoup

lineEnding = "\n"

def generateUrls(baseURL):
	url = []
	# Iterate through range of uppercase ASCII letters
	for i in range(65,91):
		url.append(baseURL + chr(i))

	return url

def getWordList(file, page):
	soup = BeautifulSoup(page.text, "lxml")
	print("Parsed HTML.")

	div = soup.find_all("div", {"class": "mw-parser-output"})
	# There is only one <div class="mw-parser-output"> per page
	# which contains the content inside a <ul>
	tagList = div[0].find_all("li")

	for item in tagList:
		file.write(item.text + lineEnding)

	print("Found {} list items.\n".format(len(tagList)))

	return len(tagList)