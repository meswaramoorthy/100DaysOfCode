# You will be given a seat number, find out the seat number facing you and the seat type, i.e. WS, MS or AS.
#
# INPUT
# First line of input will consist of a single integer T denoting number of test-cases. Each test-case consists of a single integer N denoting the seat-number.
#
# OUTPUT
# For each test case, print the facing seat-number and the seat-type, separated by a single space in a new line.
#
# CONSTRAINTS
# 1<=T<=105
# 1<=N<=108

def faceSeatNumber(seatNumber):
    """Prints facing seat number for a given seat number"""

    # seatArrangement = {(1, 12),
    #                    (2, 11),
    #                    (3, 10),
    #                    (4, 9),
    #                    (5, 8),
    #                    (6, 7),}

    seatArrangement = {1: 12, 2: 11, 3: 10, 4: 9, 5: 8, 6: 7}
#                           0   5   4   3   2   1
    # 6 - r + 1

    reverseSeatArrangement = {12: 1, 11: 2, 10: 3, 9: 4, 8: 5, 7: 6}

    seatArrangementType = {1: (12, 'WS'), 2: (11, 'MS'), 3: (10, 'AS'), 4: (9, 'AS'), 5: (8, 'MS'), 6: (7, 'WS'),
                           12: (1, 'WS'), 11: (2, 'MS'), 10: (3, 'AS'), 9: (4, 'AS'), 8: (5, 'MS'), 7: (6, 'WS')}

    qSeatNumber = seatNumber // 12
    rSeatNumber = seatNumber % 12

    # facingSeat = 0

    if rSeatNumber == 0:
        print ((qSeatNumber - 1) * 12 + seatArrangementType[12][0], seatArrangementType[12][1])
    elif rSeatNumber <= 6:
        print (qSeatNumber * 12 + seatArrangementType[rSeatNumber][0], seatArrangementType[rSeatNumber][1])
    else:
        print (qSeatNumber * 12 + seatArrangementType[rSeatNumber][0], seatArrangementType[rSeatNumber][1])


noOfTestCases = int(input())
testCases = []

for _ in range(noOfTestCases):
    testCases.append(input())

for testCase in testCases:
    faceSeatNumber(int(testCase))