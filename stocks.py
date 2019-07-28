prices = [7,1,5,3,6,4]
mn = []
neglist = []
for i in range(len(prices)-1):
    for j in range(i+1,len(prices)):
        if((prices[i]-prices[j]) < 0 ):
            neglist.append(prices[i]-prices[j])
        else:
            neglist.append(0)
    # print(neglist)
    mn.append(min(neglist))

if(len(mn)>=0):
    print(abs(min(mn)))
else:
    print(0)
        