def makeString(x):
     
    try:
        if x < 0:
            return "value is below zero"
        String = (x * "x")
        return String
    except:
        return "invalid value"


