def makeString(x):
    counter = int(x)
    string = ""
    if counter < 0 :
        raise Exception("You cannot enter a value below zero.")
    else:
        string = counter * "a"
        return string

    
