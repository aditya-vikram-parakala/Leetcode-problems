from collections import Counter
import operator
arr = [1 ,2 ,3 ,4 ,3 ,3 ,2 ,1]
l = len(arr)
op = [l]
m = min(arr)
li = []
s = sorted(Counter(arr).items(),key = operator.itemgetter(0))
for k,v in s:
    l-=v
    if l>0:
        op.append(l)
print(op)


# # print(m)

# for i in range(len(op)):
#     li.append(int(x-m) for x in op[i])
# op.append(list(li))
# print(op)
    # print(i)
# m = min(arr)
# new = []
# # for k in range(len(arr)):
# #     arr = new
# for i in range(len(arr)):
#     new.append(arr[i] - m )
# for k in new:
#     if(k==0):
#         del k
#     else:
#         new.append(k)
# print(arr)
# print(new)