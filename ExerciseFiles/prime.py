number = int(input("Enter a number"))

if number>1:
    for i in range(2,number):
        if number%i==0:
            print(number, "is not a Prime Number")
            break
        else:
            print(number,"is a Prime Number")
            break