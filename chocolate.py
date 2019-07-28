s = [4]
d = 4
m = 1
fadd = []
for i in range(len(s)-m+1):
    add = 0
    for j in range(m):
        add += s[i+j]
    fadd.append(add)
print(fadd)
cnt = 0
for i in fadd:
    if(i == d):
        cnt+=1
print(cnt)

