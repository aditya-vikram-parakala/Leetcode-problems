s = "12:35:10PM"
milclock = []
spl = s.split(":")
#print(spl)
#for i in range(len(spl[2])):
#print(spl[2][2])    
if(spl[2][2]=='P' and spl[0] != "12"):
    milclock.append(str(int(spl[0]) + 12))
    milclock.append(spl[1])
    milclock.append(spl[2])
    
elif( spl[2][2] == 'A'  and spl[0] == "12" ):
    milclock.append("00")
    milclock.append(spl[1])
    milclock.append(spl[2])
elif( spl[2][2] == 'A'  and spl[0] != "12" ):
    milclock.append(spl[0])
    milclock.append(spl[1])
    milclock.append(spl[2])

else:
    milclock = s
if(spl[2][2] == 'P' and spl[0] != "12"):
    y = ":".join(milclock)
    y = y[:-2]
    print(y)
# milclock[0] = str(milclock[0])
elif(spl[2][2] == 'P' and spl[0] == "12"):
    z = milclock[:-2]
    print(z)
else:
    x = ":".join(milclock)
    x = x[:-2]
    print(x)

