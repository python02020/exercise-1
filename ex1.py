def makeString(x):
    returnStr = ''
    if x < 0:
        raise
    else:
        for i in range(x):
            returnStr += ' '
        return returnStr 
