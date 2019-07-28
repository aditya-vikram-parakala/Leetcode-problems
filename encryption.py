import math as m
s = "feedthedog"
length = len(s)
fl = m.floor(m.sqrt(length))
cl = m.ceil(m.sqrt(length))
# mat = [[0 for i in range(cl)] for j in range(fl)]
k =0 
if((fl*cl)>=length):
    mat = [[0 for i in range(cl)] for j in range(fl)]
    for i in range(fl):
        for j in range(cl):
            if(k<(length)):
                mat[i][j] = s[k]
                k+=1

            else:
                mat[i][j] = ""
else:
    mat = [[0 for i in range(cl)] for j in range(fl+1)]
    for i in range(fl+1):
        for j in range(cl):
            if(k<(length)):
                mat[i][j] = s[k]
                k+=1

            else:
                mat[i][j] = ""

print(mat)
# for i in range(cl):
#     print(mat[:,i])
res = []
for k in range(cl):
    # print([i[k] for i in mat])
    a = "".join([i[k] for i in mat])
    # print("".join([i[k] for i in mat]))
    res.append(a)
print(*res)
        
