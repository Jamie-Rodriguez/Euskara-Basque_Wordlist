#!/usr/bin/python
import contextlib # To suppress File Not Found Exception
import os
import requests

import Scraper
import Parser

filename = "output" # Don't add .txt extension
baseURL = "URL REMOVED"

def main():
	rawFileName = filename + "_raw.txt"
	processedFileName = filename + "_final.txt"

	totalLines = 0

	# Remove file if it exists, else suppress File Not Found Exception
	with contextlib.suppress(FileNotFoundError):
		os.remove(rawFileName)

	print("Output file:\n\t{}".format(rawFileName))

	urlList = Scraper.generateUrls(baseURL)
	print("Generated URLs.")

	print("Beginning scraping.")
	print("................................................................................")
	# Scrape website and write to file
	rawFile = open(rawFileName, "a")

	for url in urlList:
		page = requests.get(url)
		# Not all URL paths are valid
		if page.status_code == 404:
			print("URL returned 404 status!\n\t{}\n".format(url))
		else:
			print("Retrieved HTML from:\n\t{}".format(url))
			try:
				totalLines += Scraper.getWordList(rawFile, page)
			except TypeError:
				totalLines += 0

	rawFile.close()

	print("\nFinished scraping!")
	print("Total items: {}\n".format(totalLines))

	# Removing spanish translations and leaving only basque words
	print("Parsing raw data file, removing spanish translations.")
	rawFile = open(rawFileName, "r")
	parsedFile = open(processedFileName, "w+")

	Parser.removeSpanish(rawFile, parsedFile)
	Parser.removeDuplicateLines(parsedFile)

	rawFile.close()
	parsedFile.close()

if __name__ == '__main__':
	main()