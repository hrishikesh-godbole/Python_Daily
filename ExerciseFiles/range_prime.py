lower_range = 100
upper_range = 1000

for number in range(lower_range, upper_range):
        if number>1:
            for i in range(2,number):
                if number%2==0:
                    break
                else:
                    print(number)
                    break