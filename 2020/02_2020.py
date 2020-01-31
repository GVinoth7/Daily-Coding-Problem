# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
# Bonus: Can you do this in one pass?

#1##################

def checkList(numList, k):

    for i in range(len(numList)):
        for j in range(i, len(numList)):
            if numList[i]+numList[j]==k and i !=j:
                return True
    return False
print(checkList([10, 15, 3, 7], 19))
