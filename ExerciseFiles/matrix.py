rows = int(input("Enter the number of rows : "))
cols = int(input("Enter the number of columns : "))

matrix = []

print("Enter the values in rows")
for i in range(rows):
    a=[]
    for j in range(cols):
        a.append(int(input()))
    matrix.append(a)

for i in range(rows):
    for j in range(cols):
        print(matrix[i][j], end=' ')
    print()