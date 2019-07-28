import math
l = []
s = "-31.4159 aaaaa"
for t in s.split():
    try:
        l.append(math.ceil(float(t)))
    except ValueError:
        pass
print(l)