def cycle_length(n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        return 1 + cycle_length(n / 2)
    
    else:
        return 1 + cycle_length(3*n + 1)

#print(cycle_length(22))

def recursive_divide(x, y):
    if x < y:
        return 0
    else:
        return 1 + recursive_divide(x-y, y)
    
#print(recursive_divide(8, 3))

def my_enumerate(items, i=0):
    if i >= len(items):
        return []
    else:
        return [(i, items[i])] + my_enumerate(items, i+1)
    
#ans = my_enumerate([10, 20, 30])
#print(ans)
#ans = my_enumerate(['dog', 'pig', 'cow'])
#print(ans)
#ans = my_enumerate([])
#print(ans)

def num_rushes(slope_height, rush_height_gain, back_sliding, start_height=0):
    if slope_height-start_height <= rush_height_gain:
        return 1
    return num_rushes(slope_height, rush_height_gain*0.95, back_sliding*0.95, start_height+rush_height_gain-back_sliding) + 1

#ans = num_rushes(10, 10, 9)
#print(ans)
#ans = num_rushes(100, 15, 7)
#print(ans)

def helper(list1, list2):
    tuples = []
    for num in list2:
        tuples.append((list1, num))
    return tuples

def all_pairs(list1, list2):
    if not (list1 and list2):
        return []
    if len(list1) == len(list2) == 1:
        return [(list1[0], list2[0])]
    mid_list1, mid_list2 = len(list1) // 2, len(list2) // 2
    return all_pairs(list1[:mid_list1], list2[:mid_list2]) + all_pairs(list1[:mid_list1], list2[mid_list2:]) + all_pairs(list1[mid_list1:], list2[:mid_list2]) + all_pairs(list1[mid_list1:], list2[mid_list2:])

#print(all_pairs([1, 2], [10, 20, 30]))


import sys
sys.setrecursionlimit(100000)

def dumbo_func(data, i=0):
    """Takes a list of numbers and does weird stuff with it"""
    if i>=len(data):
        return 0
    else:
        if (data[i] // 100) % 3 != 0:
            return 1 + dumbo_func(data, i+1)
        else:
            return dumbo_func(data, i+1)

#data = [677, 90, 785, 875, 7, 90393, 10707]
#print(dumbo_func(data, i=0))
#introduce second parameter and keep track of the index

fibs = {0: 0, 1: 1}       
def fib(n):
    if n in fibs:
        return fibs[n]
    if n % 2 == 0:
        fibs[n] = ((2*fib((n-2)/2)) + fib(n / 2)) * fib(n / 2)
        return fibs[n]
    else:
        fibs[n] = (fib((n - 1) / 2) ** 2) + (fib((n+1) / 2) ** 2)
        return fibs[n]
 
print(fib(10**6) % 10**10)
print(fib(100))


def perms(items):
    if len(items) <=1:
        yield tuple(items)
    else:
        for perm in perms(items[1:]):
            for i in range(len(items)):
                # nb items[0:1] works in both string and list contexts
                yield perm[:i] + tuple(items[0:1]) + perm[i:]

#for perm in sorted(perms([1, 2, 3])):
#    print(perm)
    
#print(perms([]))
#print(perms(['x']))

from collections import deque
 
 
# A queue node used in BFS
class Node:
    # `(x, y)` represents coordinates of a cell in the matrix
    # maintain a parent node for the printing path
    def __init__(self, x, y, parent):
        self.x = x
        self.y = y
        self.parent = parent
 
    def __repr__(self):
        return str((self.x, self.y))
 
 
# Below lists detail all four possible movements from a cell
row = [-1, 0, 0, 1]
col = [0, -1, 1, 0]
 
 
# The function returns false if pt is not a valid position
def isValid(x, y):
    return (0 <= x < N) and (0 <= y < N)
 
 
# Find the shortest route in a matrix from source cell `(x, y)` to
# destination cell `(N-1, N-1)`
def findPath(matrix, x, y):
 
    # create a queue and enqueue the first node
    q = deque()
    src = Node(x, y, None)
    q.append(src)
 
    # set to check if the matrix cell is visited before or not
    visited = set()
 
    key = (src.x, src.y)
    visited.add(key)
 
    # loop till queue is empty
    while q:
 
        # dequeue front node and process it
        curr = q.popleft()
        i = curr.x
        j = curr.y
 
        # return if the destination is found
        if i == N - 1 and j == N - 1:
            return curr
 
        # value of the current cell
        n = matrix[i][j]
 
        # check all four possible movements from the current cell
        # and recur for each valid movement
        for k in range(4):
            # get next position coordinates using the value of the current cell
            x = i + row[k] * n
            y = j + col[k] * n
 
            # check if it is possible to go to the next position
            # from the current position
            if isValid(x, y):
                # construct the next cell node
                next = Node(x, y, curr)
                key = (next.x, next.y)
 
                # if it isn't visited yet
                if key not in visited:
                    # enqueue it and mark it as visited
                    q.append(next)
                    visited.add(key)
 
    # return None if the path is not possible
    return None
 
 
# Utility function to print path from source to destination
def printPath(node):
    if node is None:
        return 0
 
    length = printPath(node.parent)
    print(node, end=' ')
    return length + 1
