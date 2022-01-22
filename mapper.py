#!/usr/bin/env python
import sys
import string

#Function to remove punctuation
def remove_punctuation(text):
    no_punct = "".join([c for c in text if c not in string.punctuation])
    return no_punct

stopwords = set(['the', 'and'])

# get all lines from stdin
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip().lower()
    line_clean = remove_punctuation(line)


    # split the line into words; splits on any whitespace
    words = line_clean.split()

    # output tuples (word, 1) in tab-delimited format
    for word in words:
	if word not in stopwords:
        	print '%s\t%s' % (word, "1")
