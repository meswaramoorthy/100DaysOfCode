# You are given an array of n numbers and q queries. For each query you have to print the floor of the expected value(mean) of the subarray from L to R.
#
#
# First line contains two integers N and Q denoting number of array elements and number of queries.
#
# Next line contains N space seperated integers denoting array elements.
#
# Next Q lines contain two integers L and R(indices of the array).
#
#
# print a single integer denoting the answer.
#
#  :
#
# 1<= N ,Q,L,R <= 10^6
#
# 1<= Array elements <= 10^9
#
# NOTE
#
# Use Fast I/O

def main():
    from sys import stdin, stdout
    n, k = stdin.readline().split()
    n = int(n)
    k = int(k)

    cnt = 0
    lines = stdin.readlines()
    for line in lines:
        if int(line) % k == 0:
            cnt += 1

    stdout.write(str(cnt))


if __name__ == "__main__":
    main()

# from sys import stdin, stdout
#
# n, q = stdin.readline().split()
#
# lines = stdin.readlines()
# # inputArray = list(map(int, input().split(' ')))
# # queryList = []
#
# # queryLines = sys.stdin.readlines()
# # queryList = list(queryLines)
# print("Completed")

# for i in range(int(q)):
#     # queryList.append(list(map(int, input().split(' '))))
#     sum = 0
#
#     startIndex, endIndex = queryList[i][0], queryList[i][1]
#     # endIndex = query[1]
#     count = int(endIndex) - int(startIndex) + 1
#
#     for i in range(int(startIndex) - 1, int(endIndex)):
#         sum += inputArray[i]
#         # print(sum)
#     # print("count =", count)
#     print(sum // count)

# n, q = input().split(' ')
#
# inputArray = list(map(int, input().split(' ')))
# queryList = []
#
# for _ in range(int(q)):
#     queryList.append(list(map(int, input().split(' '))))
#
# # print(n, q)
# # print(inputArray)
# # print(queryList)
#
# for query in queryList:
#     sum = 0
#     startIndex = query[0]
#     endIndex = query[1]
#     count = endIndex - startIndex + 1
#
#     for i in range(startIndex - 1, endIndex):
#         sum += inputArray[i]
#         print(sum)
#     # print("count =", count)
#     print(sum//count)
#     # sum = [c += c for c in queryList[startIndex - 1 : endIndex - 1]]
