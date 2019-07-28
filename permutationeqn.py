p = [2,3,1]
index = []
f = []
for i in range(len(p)):
    for j in range(len(p)):
        if((i+1) == p[p[j]-1]):
            index.append(j)
for ind in index:
    print(ind+1,sep='\n')
    
