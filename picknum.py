a = [4 ,6 ,5 ,3 ,3 ,1]
sorta = list(sorted(a))
cnt = []
out = []
for i in range(len(a)):
    for j in range(len(a)):
        if(i != j):        
            if(abs(sorta[i]-sorta[j])<=1):
                cnt.append(sorta[i])
    out.append(cnt)
for i in range(len(out)):
    for j in range(len(out)):

# NOT COMPLETED NEEDS SOME UNDERSTANDING OF CROSS PRODUCT VALUES