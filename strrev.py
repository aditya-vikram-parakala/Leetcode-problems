s = "hello  world        from NY"
# s = s.strip()
# length = len(s)
# l = list(s)
# #l[3] = "K"
# #f = ''.join(l)
# new =[]
# index=[]
# cnt = 0
# for i in range(length-1,-1,-1):
#     if(l[i]== " "):  
#         index.append(i)
#         #cnt+=1
#         #if(cnt>1):
#         #   del i
#         #new.append(i)
#     else:
#         new.append(l[i])
#         #print(i)
# index = [length-i for i in index] 
# print(index)
# for k in range(len(index)-1):
#     if(index[k]+1 == index[k+1]):
#         del index[k]    
# for i in index:
#     new.insert(i-1," ")
# print(''.join(new))
# #print(index)
# #print(l[0])
spl = s.split(' ')
print(spl)
new =[]
for k in spl:
    print(k)
    if k!='':
        new.append(k)
print(' '.join(reversed(new)))

































