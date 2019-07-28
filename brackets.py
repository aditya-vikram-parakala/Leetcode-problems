cf,cc,cs = 0, 0, 0
res = []
    for i in range(len(values)):
        for j in values[i]:
            if(j == "{"):
                cf+=1
            elif(j == '('):
                cc+=1
            else:
                cs+=1
        if(j == "}"):
            cf-=1
            if(cf==0):
                res.append(cf)
        elif(j== ")"):
            cc-=1
            if(cc == 0):
                res.append(cc)
        else:
            cs-=1
            if(cs == 0):
                res.append(cs)
        print(res)
        