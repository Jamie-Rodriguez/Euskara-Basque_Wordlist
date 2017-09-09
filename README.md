# Python Wordlist Web Scraper
I am currently learning the Basque language, _euskara_, from northern Spain. As there is not much information available on the language, especially in English I decided to try and compile a word list of the language.

There are two web scrapers written in python designed to retrieve words from webpages and write them to a text file.
	1. The first was written using the python library _lxml_ and identifies the tag via a xpath which is unique to all the Basque words on the page.
	2. Uses the _Beautiful Soup_ library as there did not seem to be a simple way of parsing the HTML using xpaths and the _lxml_ library alone.

There is no command line argument capability, but as the scripts are very simplistic, you will only need to alter the URL variable and the output file name.

## Requirements
This code was written for Python 3
