marvel_heros = ["Spiderman","Ironman","Thor"]
dc_heros = ["Batman","Flash","Aquaman"]

print(dc_heros[1:])

del dc_heros[1]
print(dc_heros)

dc_heros.append("Flash")
print(dc_heros)

dc_heros.insert(0,"Green Arrow")
print(dc_heros)

dc_heros.remove("Flash")
print(dc_heros)

dc_heros.reverse()
print(dc_heros)

print(dc_heros.count("Batman"))

print(marvel_heros+dc_heros)