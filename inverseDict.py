invDict = {}
#Creating the inverse dictionary
def add(word, path):
    global invDict
    if invDict.get(word,False):
        if path not in invDict[word]:
            invDict[word].add(path)
    else:
        invDict[word]=set([path])
#Returns the inverse dictionary
def getDict():
    return invDict
#def print_invDict():
#    print str(invDict)
    
    
