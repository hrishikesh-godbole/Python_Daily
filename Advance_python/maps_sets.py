numbers = (1,2,3,4,5)
print(numbers)

def getSquare(num):
    return num*num

result = map(getSquare, numbers)
resultTwo = set(result)
print(resultTwo)