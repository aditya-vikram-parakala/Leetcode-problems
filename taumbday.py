cost = 0
b=3
w= 5
bc=3;wc=4;z=1
if((z>bc and z>wc) or (z == bc and z == wc) or (wc==bc)):
    cost = b*bc + w*wc
    print("in last loop1")
elif(z<bc and z<= wc and wc<bc):
    cost = b*wc + w*wc + b*z
    print("in last loop2")
elif(z<=bc and z<wc and bc<wc):
    cost = b*bc + w*bc+ w*z
    print("in last loop3")
elif( (z>bc and z<wc) and (bc<wc)):
    cost = b*bc + w*(bc+z)
    print("in last loop4")
elif( (z<bc and z>wc) and (bc>wc)):
    cost = b*(wc+z) + w*wc
    print("in last loop5")
elif(z<bc and z<wc and wc<bc):
    cost = b*wc + w*wc + b*z
    print("in last loop6")
elif(z<bc and z<wc and bc<wc):
    cost = b*bc + w*bc+ w*z
    print("in last loop")
else:
    cost = b*bc + w*wc
print(cost)
