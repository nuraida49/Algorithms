dp = {}
def lcs(s1, s2):
    if s1 == '' or s2 == '':
        return ''
    elif s1[-1] == s2[-1]:
        if (s1[:-1], s2[:-1]) not in dp:
            dp[(s1[:-1], s2[:-1])] = lcs(s1[:-1], s2[:-1])
        return dp[(s1[:-1], s2[:-1])] + s1[-1]
    else:
        if (s1[:-1], s2) not in dp:
            dp[(s1[:-1], s2)] = lcs(s1[:-1], s2)
        if (s1, s2[:-1]) not in dp:
            dp[(s1, s2[:-1])] = lcs(s1, s2[:-1])
        result1 = dp[(s1[:-1], s2)]
        result2 = dp[(s1, s2[:-1])]
        if len(result1) > len(result2):
            return result1
        else:
            return result2

## A simple test that should run without caching
#s1 = "abcde"
#s2 = "qbxxd"
#lcs_string = lcs(s1, s2)
#print(lcs_string)

#s1 = "Look at me, I can fly!"
#s2 = "Look at that, it's a fly"
#print(lcs(s1, s2))

#s1 = "abcdefghijklmnopqrstuvwxyz"
#s2 = "ABCDEFGHIJKLMNOPQRSTUVWXYS"
#print(lcs(s1, s2))

#s1 = "balderdash!"
#s2 = "balderdash!"
#print(lcs(s1, s2))

#class Item:
    #"""An item to (maybe) put in a knapsack"""
    #def __init__(self, value, weight):
        #self.value = value
        #self.weight = weight
  
    #def __repr__(self):
        #return f"Item({self.value}, {self.weight})"

    #def get_weight(self):
        #return self.weight
    
    #def get_value(self):
        #return self.value

#def max_value(items, capacity):
    #item = len(items)
    #DP = [[0 for x in range(capacity+1)] for x in range(item+1)]
    #for i in range(item+1):
        #for w in range(capacity+1):
            #if i==0 or w==0:
                #DP[i][w] = 0
            #elif items[i-1].get_weight() <= w:
                #DP[i][w] = max(items[i-1].get_value() + DP[i-1][w-items[i-1].get_weight()], DP[i-1][w])
            #else:
                #DP[i][w] = DP[i-1][w]

    #return DP[item][capacity]
## The example in the lecture notes
#items = [Item(45, 3),
         #Item(45, 3),
         #Item(80, 4),
         #Item(80, 5),
         #Item(100, 8)]
#print(max_value(items, 10)) 

import sys
sys.setrecursionlimit(2000)

class Item:
    """An item to (maybe) put in a knapsack. Weight must be an int."""
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
    
    def __repr__(self):
        """The representation of an item"""
        return f"Item({self.value}, {self.weight})"
  

def max_value(items, weight):
    items.insert(0, Item(0,0))
    n = len(items) - 1
    matrix = [[-1] * (weight + 1) for _ in range(n + 1)]
    return knapsack(items, matrix, n, weight)

def knapsack(items, matrix, index, w):
    if matrix[index][w] >= 0:
        return matrix[index][w]
    if index == 0:
        q = 0
    elif items[index].weight <= w:
        q = max(knapsack(items, matrix, index - 1, w - items[index].weight) + items[index].value,knapsack(items, matrix, index - 1, w))
    else:
        q = knapsack(items, matrix, index - 1, w)
    matrix[index][w] = q
    return q


# The example in the lecture notes
items = [Item(45, 3),
         Item(45, 3),
         Item(80, 4),
         Item(80, 5),
         Item(100, 8)]
maximum, selected_items = max_value(items, 10)
print(maximum)
# Check the returned item list with a hidden function
check_item_list(items, selected_items, maximum)
        
