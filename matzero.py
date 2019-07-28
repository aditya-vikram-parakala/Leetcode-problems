matrix = [
  [0,1,0],
  [1,1,1],
  [1,1,1]
]
pos = []
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if(matrix[i][j] == 0):
            pos.append(i)
            pos.append(j)
    # pos = tuple(pos)
print(tuple(pos))
            
# print((matrix)[0])
        