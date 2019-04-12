def makeString(intInput):
    if intInput < 0:
        raise Exception('No negative integers allowed.')
    else:
        resultString = 'a' * intInput
    return resultString