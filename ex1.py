def makeString(num):
    stringChr = "a"
    if num < 0:   #RAISING EXCEPTION IF X IS BELOW 0
        raise Exception("Number not allowed")
    else:
        stringChr = "a"*num
    
    return stringChr
    
