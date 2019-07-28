year =1918
sub = 0
if(year>=1700 and year<=1917):
    if(year%4 == 0):
        sub = (256-244)
    else:
        sub = (256-243)
elif(year>1918 and year<=2700):
    if(year%400 ==0 or (year%4 == 0 and year%100 != 0)):
        sub = (256-244)
    else:
        sub =(256 -243)
elif(year == 1918):
    if(year%400 ==0 or (year%4 == 0 and year%100 != 0)):
        sub = (256-231)
    else:
        sub =(256 -230)

date = []
date.append(str(sub))
date.append("09")
date.append(str(year))
print(".".join(date))

