from collections import Counter
arr =[1 ,2 ,3 ,4 ,5 ,4 ,3 ,2 ,1 ,3 ,4]
print(Counter(arr))
d = dict(Counter(arr))
# print(max(d.values()))
cnt  = []
for k,v in d.items():
    if(v == max(d.values())):
        cnt.append(k)
if(len(cnt)>1):
    res = sorted(cnt)[0]
else:
    res = cnt[0]
print(res)