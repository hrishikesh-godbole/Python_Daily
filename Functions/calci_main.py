import calci

choice = int(input("Enter your choice. 1.add 2.subtract 3.multiple 4.divide 5.modulus"))



if choice==1:
    print(calci.addMe(8,9))
elif choice==2:
    print(calci.subMe(5,6))
elif choice == 3:
    print(calci.mulMe(5,6))
elif choice==4:
    print(calci.divMe(5,6))
elif choice==5:
    print(calci.Mod(5,6))
else:
    print("wrong choice")