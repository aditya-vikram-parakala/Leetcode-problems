topic = ['10101',
'11100',
'11010', '00101' ]
a = int(topic[0],2)
b = int(topic[1],2)
index= []
final = []
cnt = 0
# print(bin(a|b))
for i in range(len(topic)-1):
    for j in range(i+1,len(topic)):
        c = (bin ((int(topic[i],2) | (int(topic[j],2)))))
        # for k in c:
        #     if(k == ):
        #         cnt+=1
        index.append(c.count("1"))
    # final.append(index)
for f in index:
    if(f == max(index)):
        cnt+=1
        
print(max(index))
print(cnt)


        


# b = (bin(int(topic[0]))| (bin(int(topic[1]))))
# c =(bin(a)) or (bin(b))
# print(c)
# for i in range(len(topic)-1):
#     for j in range(i+1,len(topic)):
#         if(topic[i] or topic[j])

