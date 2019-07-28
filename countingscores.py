scores = [3 ,4 ,21 ,36 ,10 ,28 ,35 ,5 ,24 ,42]
maxlen , minlen = [], []
maxlen.append(scores[0])
minlen.append(scores[0])
for i in range(1,len(scores)):
    maxlen.append((max(scores[i],maxlen[i-1])))
    minlen.append((min(scores[i],minlen[i-1])))     
cmax,cmin = 0,0
for i in range(len(scores)-1):
    if(maxlen[i]<maxlen[i+1]):
        cmax+=1
    if(minlen[i]>minlen[i+1]):
        cmin+=1
print(cmax,"",cmin)