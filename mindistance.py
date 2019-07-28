res = []
a = [1 ,3 ,4 ]
for i in range(len(a)-1):
    for j in range(1,len(a)):
        if(a[i] == a[j]):
            res.append(abs(i-j))
# ans = min(res)
n = [r for r in res if(r!=0)]
print(min(n))

# print(min(res))