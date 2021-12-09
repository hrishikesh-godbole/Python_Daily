number = int(input("Enter a number"))
prod=1
if number<0:
    print("Negative number")
elif number==0:
    print("Factorial is 1")
elif number>=1:
    for i in range(1,number+1):
        prod = prod*i
    print("Factorial of", number, "is :", prod)





