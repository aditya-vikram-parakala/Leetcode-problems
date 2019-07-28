digits = [1,2,3]
# numstr = (''.join(str(digits)))
# for d in digits:
#     numstr = ''.join([str(d)])
# print(numstr)
# pone = int(numstr)+1
# print(pone)
# for x in str(pone):
#      k = int(x)
# print(k)
# add = int(numstr)+1
# strnum = str(add)
# print([int(x) for x in str((int(''.join([str(m) for m in digits])) + 1))])
strnum = ""
for i in range(len(digits)):
    strnum+=str(digits[i])

numstr = str(int(strnum)+1)
print( [x for x in numstr])
