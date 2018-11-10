# George Whitfield 
# Hack 112 2018
# November 9 2018

import string

# copied from the 112 website
def readFile(path):
    with open(path, "rt") as f:
        return f.read()

# copied from the 112 website
def writeFile(path, contents):
    with open(path, "wt") as f:
        f.write(contents)

def createJapaneseWordDictionary(japWordsList):
    resultDict = dict()
    for line in japWordsList:
        resultDict[line[0]] = tuple(line[1:])
    return resultDict

def formatJapanese(fileString): # take the file and format it into a really nice dictionary
    result = []
    for line in fileString.splitlines():
        lineList = []
        for char in line.split('\t'):
            lineList.append(char)
        result.append(lineList)
        if lineList[0] == '': # if there is no kanji for a certain word, then 
                                # make the first element of lineList = wordReading
            lineList[0] = lineList[1]
        print(lineList)
    return result