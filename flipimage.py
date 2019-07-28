import numpy as np
A = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
rev = [] 
inv = []
final = []
for a in A:
    rev.append(list(reversed(a)))
print(rev)
# for i in range(len(rev)):
#     print(rev[i])

for i in rev:
    for j in i:
        if(j == 0):
            j=1
        else:
            j=0
        inv.append(j)
final.append(inv)

print(np.array(final).reshape(len(rev),len(rev[0])))


