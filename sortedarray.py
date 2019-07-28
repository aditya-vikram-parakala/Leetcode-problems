temp = []
nums1 = [1,3]
nums2= [2]
# nums1.append(nums2)
# temp.append(nums1)
# temp.append(nums2)
for i in nums1:
    temp.append(i)
for j in nums2:
    temp.append(j)
srt = sorted(temp)
# print(srt[(len(srt)-1)//2])

if(len(srt)%2 == 0 ):
    med = (srt[(len(srt)-1)//2] + srt[((len(srt)-1)//2)+1])/2.0
else:
    med = srt[len(srt)//2]
print(med)
        