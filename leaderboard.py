scores = [100 ,90 ,90 ,80 ,75 ,60]
alice = [50 ,65 ,77 ,90 ,102]
temp= list(set(scores))  #list(set(scores))
# print(ss)
ind = []
res = []
for i in alice:
    temp.append(i)
    temp = sorted(list(set(temp)),reverse=True)
    for j in temp:
        if(i == j):
            ind.append(temp.index(j)+1)
print(temp)
print(ind)
            
    






# for i in scores:
#     bvalues.append(i)
# for i in alice:
#     bvalues.append(i)
# bsort = list(sorted(set(bvalues),reverse=True))
# print(bsort)
# for i in range(len(bsort)):
#     for j in alice:
#         if(j == bsort[i] and i!= 0 ):
#             res.append(i)
#         elif(j == bsort[i] and i== 0):
#             res.append(1)
#         elif(j == )
# print(res)

# # for i in range(len(alice)):
# #     for j in range(len(ss)):
# # bvalues.append(alice)
# # bvalues.append(scores)

#         # if(alice[i]<ss[j]):
#         #     if(j == len(ss)-1):
#         #         # print("True")
#         #         scores.insert(len(scores),alice[i])
#         #     elif(alice[i]<ss[j] and alice[i]>s[j+1]):

# # print(bvalues)
