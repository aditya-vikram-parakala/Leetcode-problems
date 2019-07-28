c = [0, 0 ,0, 0, 1 ,0 ]
# k =2
# e =100

# for i in range(0,len(c),2):
#     if(c[i]== 0):
#         e-=1
#     else:
#         e-=3
# print(e)
cnt = 0
for i in range(0,len(c),2):
    if(c[i]==0):
        cnt+=1
    else:
        i-=1
print(cnt)

