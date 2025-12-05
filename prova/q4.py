import random


n = 3
max = 100
min = -100

matrix = []
for y in range(n):
    row = []
    for x in range(n):
        row.append(random.randint(min, max))
    matrix.append(row)

for i in matrix:
    print(i)

sum = 0
for i in range(n):
    sum += matrix[i][i]

print(sum) 
sum = 0

for i in range(n):
    sum += matrix[2-i][i]
print(sum)