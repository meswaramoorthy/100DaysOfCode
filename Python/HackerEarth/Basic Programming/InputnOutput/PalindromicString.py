def palindromicStringOp(inputString):
    """Returns true if palindromic string"""
    inputStringList = list(inputString)
    flag = False

    for i in inputStringList:
        j = inputStringList.pop()
        if i == j:
            flag = True
            continue
        else:
            flag = False
            break

    return flag

def palindromicStringOp2(inputStr):
    """Take 2"""

    strList1 = list(inputString)
    strList1.reverse()
    reverseString = "".join(strList1)

    if inputString == reverseString:
        return True
    else:
        return False

inputString = input()
# print("YES" if palindromicStringOp(inputString) else "NO")
print("YES" if palindromicStringOp2(inputString) else "NO")

