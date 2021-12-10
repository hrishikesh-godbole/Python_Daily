import random

heros = ["batman","hulk","thor"]

for h in heros:
    print(h)


def hrishi():
    for i in range(10):
        yield random.randint(1,20)

for val in hrishi():
    print("Value is : ",val)
