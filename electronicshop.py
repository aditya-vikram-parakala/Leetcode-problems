key = [4]
drives = [5]
b = 5
sol = []
for i in range(len(key)):
    for j in range(len(drives)):
        if(key[i]+drives[j]<=b):
            sol.append(key[i]+drives[j])
        else:
            sol.append(-1)
if(max(sol)<=b):
    s = max(sol)
else:
    s = -1

print(s)