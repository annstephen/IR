import os
import fnmatch
import inverseDict
import re
fileName = {}
#Create the inverse dictionary
def process(dr):
    global fileName
    i=0
    #assumes nsf-awards-abstracts is the python folder
    for dirpath, dirs, files in os.walk(dr):
        for eFile in fnmatch.filter(files, '*.txt'):
            i=i+1
            fle = dirpath+"/"+eFile
            fileName[fle]=re.sub('.txt','',eFile)
            if os.path.isfile(fle) and fle != None:
                with open(fle,'r') as myfile:
                    data=" ".join(line.rstrip() for line in myfile)
                data = re.sub(r'[^a-zA-Z0-9]',' ', data)
                words = data.split()
                for word in words:
                    word = word.lower()
                    if word != "":
                        inverseDict.add(word,fle)
    print "Files : "+str(i)
#returns a dictionary matching full file names to file stem
def getFileDict():
    return fileName
