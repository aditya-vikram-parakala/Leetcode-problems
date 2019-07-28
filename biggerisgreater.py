from itertools import permutations
w = "zyyxwwtrrnmlggfeb"
nxt = [ "".join(a) for a in permutations(w)]
# if(w ==nxt[1]):
#     val = "no answer"
# else:
#     val = nxt[1]
# print(sorted(nxt))
snxt =(sorted(nxt))
indx = snxt.index(w)
# print(indx)
# print(snxt)
# MEMORY ERROR DUE TO LARGE NUMBER OF PERMUTATIONS
try:
    val = snxt[indx+1]
    for i in range(indx+1,len(snxt)):
        if(snxt[i]!= w):
            val = snxt[i]
            break
    if(val==w):
        val = "no answer"
except:
    val = "no answer"
print(val)