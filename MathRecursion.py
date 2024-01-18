
# testing data/inputs
numbers = [1, 4, 5, 2, 9, 7, 3, 5, 3, 8]
numbers2 = [7, 7, 3]
numbers3 = [9, 2, 4, 2, 2, 6, 8]


# sum of all odd numbers
def oddRecurse(numList):
    result = oddRecurseInner(0, numList)
    if len(numList) == 0:
        return 0
    return result

def oddRecurseInner(currI, lst):
    if currI == len(lst):
        return 0

    sum = oddRecurseInner((currI + 1), lst)
    if lst[currI] % 2 != 0:
        sum += lst[currI]
    return sum

print("Odd Results")
print(oddRecurse(numbers))
print(oddRecurse(numbers2))
print(oddRecurse(numbers3))


# product of all even numbers
def evenRecurse(numList):
    result = evenRecurseInner(0, numList)
    if result == 1 or len(numList) == 0:
        return 0
    return result

def evenRecurseInner(currI, lst):
    if currI == len(lst):
        return 1

    product = evenRecurseInner((currI + 1), lst)
    if lst[currI] % 2 == 0:
        product *= lst[currI]
    return product


print("Even Results")
print(evenRecurse(numbers))
print(evenRecurse(numbers2))
print(evenRecurse(numbers3))

