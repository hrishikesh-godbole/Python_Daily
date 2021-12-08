def addMe(*num):
    # total = num1 + num2
    # return total
    total =0
    for var in num:
        total = total + var
    return total

print(addMe(1,2,3,4,5,6,7,8,9,10))

#challenge solution
def bizarre(*num):
    init_price= 100
    for i in num:
        init_price = init_price - (i)
    return init_price

print(bizarre(45,34))

