#! /usr/bin/env python3

import sys
import re
import os
import subprocess
import string

if len(sys.argv) != 3:
    print("Correct usage: wordCount.py <input text file> <output file>")
    exit()

document = open(sys.argv[1], "r")
output = open(sys.argv[2], "w+")

wordsDict = dict()

for line in document:
    line = line.translate(line.maketrans(string.punctuation,' ' * len(string.punctuation)))
    line = line.strip()
    line = line.lower()
    words = line.split(" ")

    for word in words:
        if word in wordsDict:
            wordsDict[word] += 1
        else:
            wordsDict[word] = 1

for key in sorted(list(wordsDict.keys()))[1:]:
    output.write(key + " " + str(wordsDict[key]) + "\n")
output.close()
