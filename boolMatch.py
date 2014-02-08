import textPro
import inverseDict
import time
import re
invDict = {}
#Generates a list of files that contain all the terms in the query
def match(instring):
    global invDict 
    invDict = inverseDict.invDict
    instring = re.sub(r'[^a-zA-Z0-9]',' ', instring)
    instring = instring.lower()
    words = instring.split()
    result = []
    for word in words:
        if invDict.get(word,False) and len(result) == 0:
            result = invDict[word]
        elif invDict.get(word, False):
            result = result.intersection(invDict[word])
        else:
            result = []
            break
    return result
dr = raw_input("Enter the directory of the repository : ")
dr = str(dr)
start = time.time()
#Generate Inverse Dictionary       
textPro.process(dr)
end = time.time()
print "Process time : "+ str(end-start)
user_input = raw_input("Enter String (-1 to Exit)")
start1 = time.time()
while(str(user_input) != '-1'):
    result = match(user_input)
    #Prints error statement for empty result
    if result == []:
        print "sorry, no match"
    #Prints list of files
    else:
        fileName = textPro.fileName
        i = 0
        #restricts output to 50 files
        for fle in result:
            if i<50:
                print fileName[fle]
                i = i+1
            else:
                break
    end1 = time.time()
    print "Process time : "+str(end1-start1)
    user_input = raw_input("Enter String (-1 to Exit)")
    start1 = time.time()
