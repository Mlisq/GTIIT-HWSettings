#import numpy as np

inputValue = input("Please input the n t d b (Using space to split each number)").split(' ')

for i in inputValue:
    if i == '':
        inputValue.remove(i)
        
sizeNum = (int)(inputValue[0])

matrix = [[(inputValue[2])] * sizeNum for i in range(sizeNum)]

for i in range(sizeNum):
    for j in range(sizeNum):
        if i == j:
            continue
        if j > i :
            matrix[i][j] = (inputValue[1])
        if j < i :
            matrix[i][j] = (inputValue[3])
        

print(matrix)