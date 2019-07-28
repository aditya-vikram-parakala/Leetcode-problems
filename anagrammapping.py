A = [12, 28, 46, 32, 50]
B = [50, 12, 32, 46, 28]
ind = []
for i in A:
    if i in B:
        ind.append(B.index(i))
print(ind)