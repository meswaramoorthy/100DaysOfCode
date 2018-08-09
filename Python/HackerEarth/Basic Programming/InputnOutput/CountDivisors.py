inputList = list(map(int,input().split(' ')))

l = inputList[0]
r = inputList[1]
k = inputList[2]

multiplesList = [d for d in range(l,r+1) if d % k == 0]

print(len(multiplesList))

# remainder1 = l % k
# remainder2 = r % k
#
# print(remainder1, remainder2)
#
# start = l + (k - remainder1)
# end = r - remainder2
#
# print((end - start)//k)