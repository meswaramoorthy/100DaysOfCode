arraySize = int(input())

productValue = 1
arrayInput = map(int, input().split(' '))

for arrayValue in arrayInput:
    productValue *= arrayValue

print(productValue % (10**9 + 7))