s = 'aba'
n =10
ss = []
cnt = 0
for i in range(n):
    ss.append(s[i%len(s)])
# print(ss) 
final = ''.join(ss)
for i in final:
    if(i == 'a'):
        cnt+=1
print(cnt)