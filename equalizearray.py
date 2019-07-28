arr = [1,2,3,4,5]
from collections import Counter

cnt = dict(Counter(arr))
m = max(cnt.values())
res = 0

for k,v in cnt.items():
    if(v != m):
        res+=v


print(res)