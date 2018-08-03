# input=input()
# output = ''
# for c in input:
#     if c=='G':
#         output+='C'
#     elif c=='C':
#         output += 'G'
#     elif c=='T':G
#         output += 'A'
#     elif c=='A':
#         output+='U'
#     else:
#         output='Invalid Input'
#         break
# print(output)


a="GCTA"; b="CGAU"
c = input()
try:print(''.join(b[a.index(i)]for i in c))
except:print('Invalid Input')