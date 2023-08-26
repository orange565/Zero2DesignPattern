print("_____________ SORT UNSORTED LIST _____________________\n")

def removeSmallest(smallest, list):
    # Remove the smallest number from the given list 
    newList = []
    for i in list:
        if(i != smallest):
            newList.append(i)      
    return newList

def findSmallest(list):
    # Find the smallest number from the given list 
    smallest = -1
    for i in list:
        if smallest == -1:
            smallest = i
        else:
            if smallest >i:
                smallest = i
    return smallest

numList = [3, 1, 5, 4, 0, 1, 8, 6, 7, 9, 2,11,17,20]
#numList = [3, 1]
resultList = []

print("Unsorted List = ", numList,"\n")
while numList:
    smallestNum = findSmallest(numList)
    resultList.append(smallestNum)
    numList = removeSmallest(smallestNum, numList)

print("Sorted List = ", resultList)

print("\n_____________ SUM NUMBER IN A LIST ______________\n")

def sumList(list):
    # Sum all numbers in the list
    result = 0
    for num in list:
        result += num
    return result

list = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
print("Sum of the this list ", list, " is = ", sumList(list))

print("\n_____________ REMOVE DUPLICATES FROM THE LIST ______________\n")

list = [1, 5, 7, 9, 7, 1, 5, 3, 8, 7, 6, 3, 4, 4, 1, 5, 2, 2, 3]

def removeDuplicates(list):
    # Remove the duplicates from the given list
    resultList = []
    for num in list:
        if num not in resultList:
            resultList.append(num)
    return resultList

print("Removed duplicates from this list ", list)
print("This is the result = ",removeDuplicates(list))


print("\n_____________ FIND NAMES THAT HAVE LESS THAN 6 CHAR ______________\n")
names = ["makbule", "duru", "fatih", "ahmet", "rumeysa", "huseyin", "isa", "melahat", "gorkem"]

def findNames(list, maxLength):
    #Find names with length less than given maxLength
    returnList = []
    for name in list:
        if len(name) < maxLength:
            returnList.append(name)
    return returnList
print("Find the names that have less than 6 char from this list ", list)
print("This is the result, ",findNames(names,6))

print("\n_____________________ THE END __________________________\n")