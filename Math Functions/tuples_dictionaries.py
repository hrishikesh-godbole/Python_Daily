# marvel_heros = ("Spiderman","Ironman","Thor")
# dc_heros = ("Batman","Flash","Aquaman","Green Arrow")
#
# email = ("anish",)
# print(email)
#
# heros = marvel_heros + dc_heros
# print(heros)

# dictionaries

marvel_heros = {
    "Spiderman": 90,
    "Ironman": 95,
    "Thor": 78
}

dc_heros = {
    "Batman": 91,
    "Flash": 80,
    "Aquaman": 87
}

print(len(dc_heros))
# print(dc_heros.clear())
# print(dc_heros)

dc_heros.update(marvel_heros)
print(dc_heros)

myTags = ("Name","Last Name","Age","Phone")

myOne = dict.fromkeys(myTags)
print("My dictionary is : %s" %str(myOne))