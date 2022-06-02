def key_positions(seq, key):
    k = max(key(a) for a in seq)
    C = [0 for i in range(k+1)]
    for i in range(0, k):
        C[i] = 0
    for a in seq:
        C[key(a)] = (C[key(a)]) + 1
    sum = 0
    for i in range(0, k+1):
        C[i], sum = sum, sum+C[i]
    return C
    
#print(key_positions([0, 1, 2], lambda x: x))
#print(key_positions([2, 1, 0], lambda x: x))
#print(key_positions([1, 2, 3, 2], lambda x: x))
#print(key_positions([5], lambda x: x))
#print(key_positions(range(-3,3), lambda x: x**2))
#print(key_positions(range(1000), lambda x: 4))
#print(key_positions([1] + [0] * 100, lambda x: x))

def sorted_array(seq, key, positions):
    n = len(seq)
    B = [0]*n
    for a in seq:
        B[positions[key(a)]] = a
        positions[key(a)] = positions[key(a)] +1
    return B

#print(sorted_array([3, 1, 2], lambda x: x, [0, 0, 1, 2]))
#print(sorted_array([3, 2, 2, 1, 2], lambda x: x, [0, 0, 1, 4]))
#print(sorted_array([100], lambda x: x, [0]*101))
#"""Counting Sort"""
#import operator

#def counting_sort(iterable, key):
#    positions = key_positions(iterable, key)
#    return sorted_array(iterable, key, positions)
    
#objects = [("a", 88), ("b", 17), ("c", 17), ("d", 7)]

#key = operator.itemgetter(1)
#print(", ".join(object[0] for object in counting_sort(objects, key)))

def key_positions(seq, key):
    k = max(key(a) for a in seq)
    C = [0 for i in range(k+1)]
    for i in range(0, k):
        C[i] = 0
    for a in seq:
        C[key(a)] = (C[key(a)]) + 1
    sum = 0
    for i in range(0, k+1):
        C[i], sum = sum, sum+C[i]
    return C
    
def sorted_array(seq, key, positions):
    n = len(seq)
    B = [0]*n
    for a in seq:
        B[positions[key(a)]] = a
        positions[key(a)] = positions[key(a)] +1
    return B

def counting_sort(iterable, key):
    positions = key_positions(iterable, key)
    return sorted_array(iterable, key, positions)
        
#print(counting_sort([329, 457, 657, 839, 436, 720, 355], 3))
#print(radix_sort([329, 457, 657, 839, 436, 720, 355], 1))
#print(radix_sort([329, 457, 657, 839, 436, 720, 355], 2))

def sort(UnsortedList,position):
    bucket = []#this list will contain 10 list , each list is for every digit
    for i in range(0,10):
        poslist = []#list for integer i
        bucket.append(poslist)

    for num in UnsortedList:
        numstr = str(num)#converting number into string
        posval = 0
        if(len(numstr) >= position):#if number length is greater than equal to position
            #ord() function give ASCII value of the character
            #numstr[-position] will give the "position"th character from left 
            posval = ord(numstr[-position]) - ord('0') #getting the value of "position" digit in every number in the list
            bucket[posval].append(num)#appending the number in the respective list [ if number is zero means the number will be appended into first list, if number is 1 then in 2nd list]
        else:
            bucket[0].append(num)

    sortedList = []#list will contain the numbers sorted according to the position 

    #adding the numbers in sortedList from bucket
    for poslist in bucket:
        for num in poslist:
            sortedList.append(num)

    return sortedList
    
def radix_sort(numbers, d):
    finalList = numbers
    for position in range(1,d+1):#call sort function for position 1 to maxpos
        finalList = sort(finalList, position)

    return finalList


print(radix_sort([329, 457, 657, 839, 436, 720, 355], 3))
print(radix_sort([329, 457, 657, 839, 436, 720, 355], 1))
print(radix_sort([329, 457, 657, 839, 436, 720, 355], 2))
print(radix_sort([9, 57, 657], 1))
print(radix_sort([9, 57, 657], 2))
print(radix_sort([9, 57, 657], 3))