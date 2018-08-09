# Given two strings, a and b , that may or may not be of the same length, determine the minimum number of character
# deletions required to make a and b anagrams. Any characters can be deleted from either of the strings.
# #
# # Input :
# #
# # test cases,t
# # two strings a and b, for each test case
# # Output:
# #
# # Desired O/p
# #
# # Constraints :
# #
# # string lengths<=10000
# #
# # Note :
# #
# # Anagram of a word is formed by rearranging the letters of the word.
# #
# # For e.g. -> For the word RAM - MAR,ARM,AMR,RMA etc. are few anagrams.

def commonStringOperation(commonString, str1 , str2):
    """Compares the string for repetitive characters"""

    print("{} {} ".format("Common String is ", commonString))
    noOfdeletions = 0
    repStr = []

    if(len(commonString) == 0):
        print("Emopty Common String")
        return len(str1) + len(str2)

    for char in commonString:
        repStr.append(char)
        repCount = str1.count(char)
        repCount2 = str2.count(char)

        if repCount > 1 and repStr.count(char) == 1:

            if(repCount == repCount2):
                """No deletion required."""
                continue
            elif repCount < repCount2:
                noOfdeletions += repCount2 - repCount
            else:
                noOfdeletions += repCount - repCount2
        elif repCount2 > 1 and repStr.count(char) == 1:
            repStr.append(char)
            noOfdeletions += repCount2 - 1

    print(repStr)
    return noOfdeletions

            # if (repCount == repCount2):
            #     """No deletion required."""
            #     continue
            # elif repCount < repCount2:
            #     noOfdeletions += repCount2 - repCount
            # else:
            #     noOfdeletions += repCount - repCount2


def anagramStringOperations(str1, str2):
    """REturns the minimum number of character deletion required to make str1 and str2 anagrams"""

    strCommon1 = [char for char in str1 if char in str2]
    strCommon2 = [char for char in str2 if char in str1]

    print(strCommon1, strCommon2)

    count1 = len(strCommon1)
    count2 = len(strCommon2)

    noOfCommonDeletions = 0
    noOfTotalDeletions = 0

    if count1 < count2:
        noOfCommonDeletions = commonStringOperation(strCommon1, str1, str2)
        noOfTotalDeletions = len(str1) - len(strCommon1) + noOfCommonDeletions
    elif count1 > count2:
        noOfCommonDeletions = commonStringOperation(strCommon2, str1, str2)
        noOfTotalDeletions = len(str2) - len(strCommon2) + noOfCommonDeletions
    else:
        if len(str1) <= len(str2):
            noOfCommonDeletions = commonStringOperation(strCommon1, str1, str2)
            noOfTotalDeletions = len(str1) - len(strCommon1) + noOfCommonDeletions
        elif len(str1) > len(str2):
            noOfCommonDeletions = commonStringOperation(strCommon2, str1, str2)
            noOfTotalDeletions = len(str2) - len(strCommon2) + noOfCommonDeletions
        # else


    print(noOfCommonDeletions)
    print(noOfTotalDeletions)


def anagramStringOp(str1, str2):
    """Take 2"""

    strCommon = [char for char in str1 if char in str2]

    """Delete excess from str1"""
    deletionCount1 = len(str1) - len(strCommon)

    """Delete excess from str2"""
    strNotCommon = [char for char in str2 if char not in strCommon]
    deletionCount2 = len(strNotCommon)

    deletionCount3 = 0
    repList = []
    for char in strCommon:
        repList.append(char)
        if repList.count(char) == 1:
            count1 = str1.count(char)
            count2 = str2.count(char)

            # print(char + str(count1) + str(count2))

            if count1 == count2:
                continue
            elif count1 > count2:
                deletionCount3 += count1 - count2
            else:
                deletionCount3 += count2 - count1

    print("Common String is {0}, Count1 = {1}, Count2 ={2}, Count3 ={3}".format(strCommon, deletionCount1,
                                                                                deletionCount2, deletionCount3))

    return deletionCount1 + deletionCount2 + deletionCount3

def anagramStringOp2(str1, str2):
    """Take 3 on the pbm. Returns the total deletion required"""
    """Much better and optimised method"""

    strLength1 = len(str1)
    strLength2 = len(str2)

    strList1 = list(str1)
    strList2 = list(str2)

    commonCharCount = 0

    for ch in strList1:
        if ch in strList2:
            commonCharCount += 1
            strList2.remove(ch)

    return strLength1 + strLength2 - 2*commonCharCount


    # l1 = len(s1)
    # l2 = len(s2)
    # li1 = list(s1)
    # li2 = list(s2)
    # c = 0
    # for i in range(l1):
    #     if li1[i] in li2:
    #         c += 1
    #         li2.remove(li1[i])
    #
    # print(l1, l2, c)
    # return l1+l2-2*c

noOfTestCases = int(input())
testCases = []

for _ in range(noOfTestCases):
    testCases.append((input(), input()))

for testCase in testCases:
    print(anagramStringOp2(testCase[0], testCase[1]))
    # anagramStringOperations(testCase[0], testCase[1])
    # deletionCount1 = anagramStringOp(testCase[0], testCase[1])
    # deletionCount2 = anagramStringOp(testCase[1], testCase[0])

    # print(min(deletionCount1, deletionCount2) , take3(testCase[0], testCase[1]))