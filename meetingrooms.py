intervals = [[7,10],[2,4],[5,9],[8,13]]
s = sorted(intervals)
cnt = 1
for i in range(len(intervals)-1):
    if(s[i][1]<s[i+1][0]):
        continue
    else:
        cnt+=1

print(cnt)