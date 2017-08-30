#!/usr/bin/python
import contextlib # To suppress File Not Found Exception
import os
import requests
from bs4 import BeautifulSoup

filename = "output.txt"

def generateUrls():
	baseURL = "URL REMOVED"
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
		file.write(item.text + '\n')
	print("Found {} list items.\n".format(len(tagList)))

if __name__ == '__main__':
	# Remove file if it exists, else suppress File Not Found Exception
	with contextlib.suppress(FileNotFoundError):
		os.remove(filename)

	print("Output:\n\t{}".format(filename))

	urlList = generateUrls()
	print("Generated URLs.")

	file = open(filename, "a")

	for url in urlList:
		page = requests.get(url)
                # Not all URL paths are valid
		if page.status_code == 404:
			print("URL returned 404 status!\n\t{}\n".format(url))
		else:
			print("Retrieved HTML from:\n\t{}".format(url))
			getWordList(file, page)

	file.close()
