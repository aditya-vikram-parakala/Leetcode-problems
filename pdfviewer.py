h = [1 ,3 ,1 ,3 ,1 ,4 ,1 ,3 ,2 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,5 ,7]
word = "zabc"
print(list(word))
lw =list(word)
length = []
for i in range(len(lw)):
    length.append(h[ord(lw[i]) - 97])
mval = max(length)
area = (mval*(len(lw)))
print(area)