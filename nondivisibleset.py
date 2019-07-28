ans  = []
# S = [278 ,576 ,496 ,727 ,410 ,124 ,338 ,149 ,209 ,702 ,282 ,718 ,771 ,575 ,436]
S = [1,7,2,4]
k = 3
for i in range(len(S)-1):
    for j in range(i+1,len(S)):
        if((S[i]+S[j] % k) != 0):
            ans.append(S[i])
            ans.append(S[j])
new = list(set(ans))

    
    