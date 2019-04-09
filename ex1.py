def makeString(x):
    returnString = ""
    if x<0:
        raise Exception("No negatives allowed!")
    for i in range(0, x):
        returnString += "a"
    return returnString
    
