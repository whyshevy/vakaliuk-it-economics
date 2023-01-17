#Bohdan Vakaliuk FICT 2019 All rights are reserved. ©

#creating a matrix

import random
size = int(input("Enter size: "))
matrix = [[random.randrange(-10,10) for y in range(size)] for x in range(size)]
print("First matrix is: ", matrix)

#finding the biggest element

def find_max(size):
    list = []
    max_el = -11
    big_x = 0
    big_y = 0
    for a in range(size):
        for b in range(size):
            if abs(matrix[a][b]) > max_el:
                max_el = abs(matrix[a][b])
                big_x = a
                big_y = b
    list.append(max_el)
    list.append(big_x)
    list.append(big_y)
    return list

result = find_max(size)
max_el = result[0]
big_x = result[1]
big_y = result[2]

print("Maximum element is: ", max_el)
print("Its row is: ", big_x)
print("Its column is: ", big_y)

#changing the matrix

del matrix[find_max(size)[1]]
for i in range(size - 1):
    del matrix[i][big_y]
print("New matrix is: ", matrix)
