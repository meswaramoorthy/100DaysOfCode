# You are given an integer N. You need to print the series of all prime numbers till N.
#
# Input Format
#
# The first and only line of the input contains a single integer N denoting the number till
# where you need to find the series of prime number.
#
# Output Format
#
# Print the desired output in single line separated by spaces.
#
# Constraints
#
# 1<=N<=1000

def primeNumberSeries2(n):
    """another variation returns prime numnber sequence upto n"""
    import math

    primeNumberList = [2]
    finalCheck = round(math.sqrt(n))
    prime = False

    for i in range(2, n+1):
        for d in primeNumberList:
            if d > finalCheck:
                break
            if i % d == 0:
                prime = False
                break
            else:
                prime = True
                continue

        if prime:
            primeNumberList.append(i)
        else:
            continue

    return primeNumberList

def primeNumberSeries(n):
    """returns a list with prime numbers starting with 2 upto n"""

    primeNumberList = [2]
    prime = False

    for i in range(2, n+1):
        for d in primeNumberList:
            if i % d == 0:
                prime = False
                break
            else:
                prime = True
                continue

        if prime:
            primeNumberList.append(i)
        else:
            continue

    return primeNumberList


n = input()

primeList = primeNumberSeries2(int(n))

for prime in primeList:
    print(prime, end=' ')


