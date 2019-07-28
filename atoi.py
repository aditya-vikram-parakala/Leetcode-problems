ip = "3.14159"
# clean = ip.replace(" ","")
clean = ip.strip()
ul = (2**31)-1
ll = -(2**31)
print(clean)
try:
    if(clean[0] =='-'):
        clean = clean.replace("-","")
        k = [float(s) for s in clean.split() if s.isdigit()]
        # print(-k[0])
        res = -k[0]
    elif(float(clean[0])>0):
        k = [float(s) for s in clean.split() if s.isdigit()]
        # print(k[0])
        res = k[0]

    if(res<=ul and res>=ll):
        print(res)
    elif(res<ll):
        print(ll)
    else:
        print(ul)
except:
    print(0)


# k = [int(s) for s in clean.split() if s.isdigit()]
# print(k)
# num = [0,1,2,3,4,5,6,7,8,9]
# result = []
# for i in clean:
#     for j in num:
#         # if(i == '-'):
#         #     result.append(i)
#         try:
#             if(int(i)==j or i=='-'):
#                 result.append(i)
#             else:
#                 break
#         except:
#             break
        
# print(result)