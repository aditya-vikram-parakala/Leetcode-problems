emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
# listlen = len(emails)
# final = [] 
# word = []
# ind = []
# # for i in emails:
# for k in range(listlen):
#     for l in range(len(emails[k])):
#         if(emails[k][l] == '+' or emails[k][l] == '@'):
#             ind.append(l)
#     #     else:
#     #         word.append(emails[k][l])
# #final.append(ind)
# for i in range(0,len(ind),2):
#     print(ind[i:i+2])
#     print(emails[ind[i:i+2]])
final = set()
for email in emails:
    #print(email.split('@'))
    loc,dom = email.split('@')
    if '+' in loc:
        loc = loc[:loc.index('+')]
    final.add(loc.replace('.','')+'@'+dom)
print(len(final))