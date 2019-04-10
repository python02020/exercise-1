def makeString(intInput):
    s = ""
    try:
        if intInput > 0:
            result = "a" * intInput
            return result
        elif intInput == 0:
            return s
        elif intInput < 0:
            print("Error! No negative integers allowed.")
            return None
    except:
        print("Input is not an integer")