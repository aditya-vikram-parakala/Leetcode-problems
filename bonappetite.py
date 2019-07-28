bill = [3,10,9,2] 
k = 1
b = 7
# act = 0
del bill[k]
# print(bill)
act = int(sum(bill)/2)
# print(act)
if(act == b):
    print("Bon Apeptit")
else:
    print(b - act)