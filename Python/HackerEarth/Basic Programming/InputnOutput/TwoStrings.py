# Given two strings of equal length, you have to tell whether they both strings are identical.
#
# Two strings S1 and S2 are said to be identical, if any of the permutation of string S1 is equal to the string S2. See Sample explanation for more details.
#
# Input :
#
# First line, contains an intger 'T' denoting no. of test cases.
# Each test consists of a single line, containing two space separated strings S1 and S2 of equal length.
# Output:
#
# For each test case, if any of the permutation of string S1 is equal to the string S2 print YES else print NO.
# Constraints:
#
# 1<= T <=100
# 1<= |S1| = |S2| <= 10^5
# String is made up of lower case letters only.
# Note : Use Hashing Concept Only . Try to do it in O(string length) .

# def hashFunc(char):
#     """Hash function"""
#     return char - 'a'

def frequencyStringOp(str):
    """Returns dict for the str"""

    frequencyStr = {}

    for ch in str:
        # key = hashFunc(ch)
        # frequencyStr[ch] += 1
        if ch in frequencyStr.keys():
            frequencyStr[ch] += 1
        else:
            frequencyStr[ch] = 1

    return frequencyStr

def stringOp(str1, str2):
    """Returns YES if identical according to pbm else NO"""

    frequency1 = frequencyStringOp(str1)
    frequency2 = frequencyStringOp(str2)

    # print(frequency1)
    # print(frequency2)

    if(frequency1 == frequency2):
        return "YES"
    else:
        return "NO"

noOfTestCases = int(input())

testCases = []

for _ in range(noOfTestCases):
    testCases.append(list(input().split(' ')))

for testCase in testCases:
    # print(stringOp(testCase[0], testCase[1]))
    if sorted(testCase[0]) == sorted(testCase[1]):
        print("YES")
    else:
        print("NO")
