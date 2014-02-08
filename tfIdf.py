import inverseDict
import math
import textPro
import fnmatch
import collections
import os
import re
import time
idfDict = {}
tfDict = {}
modFile = {}
dr = ''
N = 41333
#Calculate the idf from the inverse dictionary already created 
def idf():
    global invDict
    global idfDict
    for word in invDict:
        idfDict[word] = float(math.log10(N/len(invDict[word])))
#Calculate the term frequency from the inverse dictionary as well as the mod of each file vector
def tf():
    global modFile
    global tfDict
    global dr
    i=0
    for dirpath, dirs, files in os.walk(dr):
        for eFile in fnmatch.filter(files, '*.txt'):
            i=i+1
            fle = dirpath+"/"+eFile
            if os.path.isfile(fle) and fle != None:
                with open(fle,'r') as myfile:
                    data=" ".join(line.rstrip() for line in myfile)
                data = re.sub(r'[^a-zA-Z0-9]',' ', data)
                data = data.lower()
                words = data.split()
                tfDict[fle] = collections.Counter(words)
                modFile[fle] = 0
                for word in tfDict[fle]:
                    temp = 1 + math.log10(tfDict[fle][word])
                    modFile[fle] = modFile[fle] + math.pow(temp, 2)*math.pow(idfDict[word], 2)
                modFile[fle] = math.sqrt(modFile[fle])
    #print "Files : "+str(i)
#Matches the queries to the documents and generates the tfIdf time
def match(strng):
    strng = re.sub(r'[^a-zA-Z0-9]',' ', strng)
    #print strng
    strng = strng.lower()
    strng = strng.split()
    files = {}
    for word in strng:
        if invDict.get(word, False) and invDict[word] != '':
            if len(files) == 0:
                files = invDict[word]
            else:
                files = files.union(invDict[word])
        else:
            print "sorry,no match"
            return
    tfidf = {}
    strng = collections.Counter(strng)
    modQr = 0
    for word in strng:
        modQr = modQr + math.pow((1 + math.log10(strng[word])),2)
    modQr = math.sqrt(modQr)
    fileName = textPro.fileName
    for fle in files:
        num = 0
        for word in strng:
            if idfDict.get(word, False) and tfDict[fle].get(word,False):
                num = num + (1+math.log10(strng[word]))*(1+math.log10(tfDict[fle][word]))*idfDict[word]
        den = modFile[fle]*modQr
        tfidf[fileName[fle]] = float(num/den)
    tfidf = collections.OrderedDict(sorted(tfidf.items(), key=lambda t:t[1], reverse = True)[:50])
    for item in tfidf:
            print item, "["+str(tfidf[item])+"]"
dr = raw_input("Enter the directory of the repository : ")
dr = str(dr)
start = time.time()
#pre-processes the files to generate the inverse dictionary
textPro.process(dr)
invDict = inverseDict.getDict()
#print "No: of tokens : "+ str(len(invDict))
#Calculate the idf and tf
idf()
tf()
end = time.time()
print "process time "+str(end-start) 
user_input = raw_input("Enter String (-1 to Exit)")
start1 = time.time()
while(str(user_input) != '-1'):
    match(user_input)
    end1 = time.time()
    print "process time "+str(end1-start1)
    user_input = raw_input("Enter String (-1 to Exit)") 
    start1 = time.time()
