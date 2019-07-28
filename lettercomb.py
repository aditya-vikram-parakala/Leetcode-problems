digits = "23"
l = len(digits)
prep = []
mapping ={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
for i in range(l):
    key = str(digits[i])
    prep.append(list(mapping[key]))
final = []
import itertools
for v in itertools.product(*prep):
    final.append(str(''.join(v)))
print(final)    