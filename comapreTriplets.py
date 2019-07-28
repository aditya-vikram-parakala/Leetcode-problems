def count():
    a=[10,20,30]
    b=[20,2,4]    
    cnt,dnt =0,0
    final = []
    for i in range(len(a)):
        if(a[i]>b[i]):
            cnt +=1
            
        elif(a[i]<b[i]):
            dnt+=1
        else:
            continue
    final.append(cnt)
    final.append(dnt)
    print(final)
count()