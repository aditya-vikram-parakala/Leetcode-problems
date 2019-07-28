s = "loveleetcode"
slist = list(s)
# dt = {}
count = []
from collections import Counter
#for i in range(len(s)):
c = dict(Counter(s))
for K,v in c.items():
    if(v == min(c.values())):
        count.append(slist.index(K))
        break
print(count[-1])


# print((c[i]))    
    