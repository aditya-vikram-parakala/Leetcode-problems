i =20
j =23
k = 6
res = []
# print( abs(j - int(str(j)[::-1])))
for a in range(i,j+1):
    if( abs(a - int(str(a)[::-1])) % k == 0 ):
        res.append(a)
print(len(res))
        