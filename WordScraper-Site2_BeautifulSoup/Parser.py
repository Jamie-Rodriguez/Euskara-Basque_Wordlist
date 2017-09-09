lineEnding = "\n"

def removeSpanish(inFile, outFile):
	# Expected format:
	# <basque text> <rightwards arrow> <spanish text>
	for line in inFile:
		# The arrow is unicode character: rightwards arrow (U+2192)
		basque = line.split(u"\u2192")[0]
		basque = basque.strip()
		outFile.write(basque + lineEnding)

# Make sure file pointer is in read/write mode!!
def removeDuplicateLines(file):
	file.seek(0)
	lines = file.readlines()
	file.seek(0)

	prevLine = ""
	for line in lines:
		if line != prevLine:
			file.write(line)
			prevLine = line

	file.truncate()