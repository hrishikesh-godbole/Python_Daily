#lists

myListOne = ["One","Two","Three","Four","Ten","Hundred"]
myListTwo = [1,"Anish",3,"Five"]
print(myListOne)
print(myListTwo[1])
print(myListOne[1:4])
print(myListTwo*2)
print(myListTwo+myListOne+myListTwo)

myListOne[1] = "Fifty"
print(myListOne)

# tuples
myTupleOne = (1,"Anish",45,"Godbole")
myTupleTwo = (2,"Ram","Piyu",40)
print(myTupleOne*3)
print(myTupleTwo[2])
print(myListOne[1:3])

# you simply cannot modify tuple values
# myTupleOne[2] = 90
# print(myTupleOne)