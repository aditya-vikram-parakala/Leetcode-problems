arr = ["eat", "tea", "tan", "ate", "nat", "bat"]
res = []
final = []
print(sorted(arr))
for i in arr:
    for j in range(arr.index(i)+1,len(arr)):
        if( sorted(i) == sorted(arr[j])):
            res.append(arr[j])
    final.append(res)
print(final)
# for i in range(len(arr)):
#     for j in range(i+1,len(arr)):
#         if(sorted(arr[i]) == sorted(arr[j])):
#             res.append(arr[i])
#     final.append(res)
# print(final)