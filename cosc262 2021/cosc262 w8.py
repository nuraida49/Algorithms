def coins_reqd(value, coinage):
    """The minimum number of coins to represent value assuming a 1-unit coin"""
    num_coins = [0] * (value + 1)
    for amt in range(1, value + 1):
        num_coins[amt] = 1 + min(num_coins[amt - c] for c in coinage if amt >= c)

    # The value of the num_coins array is displayed at this point.
    return num_coins

#print(coins_reqd(440, [1, 20]))



"""A broken implementation of a recursive search for the optimal path through
   a grid of weights.
   Richard Lobb, January 2019.
"""
INFINITY = float('inf')  # Same as math.inf

def read_grid(filename):
    """Read from the given file an n x m grid of integer weights.
       The file must consist of n lines of m space-separated integers.
       n and m are inferred from the file contents.
       Returns the grid as an n element list of m element lists.
       THIS FUNCTION DOES NOT HAVE BUGS.
    """
    with open(filename) as infile:
        lines = infile.read().splitlines()

    grid = [[int(bit) for bit in line.split()] for line in lines]
    return grid


def grid_cost(grid):
    """The cheapest cost from row 1 to row n (1-origin) in the given
       grid of integer weights.
    """
    n_rows = len(grid)
    n_cols = len(grid[0])
    result = 0
    
    cost = [[None for i in range(n_cols)] for j in range(n_rows)]
    for i in range(n_cols):
        cost[0][i] = grid[0][i]
 
    for row in range(1, n_rows):
        for col in range(n_cols):
            left = cost[row-1][col-1] if (col - 1) >= 0 else INFINITY
            right = cost[row-1][col + 1] if ((col + 1) < (n_cols)) else INFINITY
            middle = cost[row-1][col]
 
            cost[row][col] = min(left, right, middle) + grid[row][col]
 
    return min(cost[-1])
    
    
def file_cost(filename):
    """The cheapest cost from row 1 to row n (1-origin) in the grid of integer
       weights read from the given file
    """
    return grid_cost(read_grid(filename))

#print(file_cost('checkerboard.trivial.in'))
#print(file_cost('checkerboard.small.in'))



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
    
def knapsack(items, matrix, index, n_weight):
    if matrix[index][n_weight] >= 0:
        return matrix[index][n_weight]

    if index == 0:
        queue = 0
    elif items[index].weight <= n_weight:
        queue = max(knapsack(items, matrix, index - 1, n_weight - 
                             items[index].weight) + items[index].value,
                knapsack(items, matrix, index - 1, n_weight))
    else:
        queue = knapsack(items, matrix, index - 1, n_weight)
    matrix[index][n_weight] = queue
    return queue
    
    
def max_value(items, weight):
    items.insert(0, Item(0,0))
    n = len(items) - 1
    matrix = [[-1] * (weight + 1) for _ in range(n + 1)]
    return knapsack(items, matrix, n, weight)    

## The example from the lecture notes
#items = [
    #Item(45, 3),
    #Item(45, 3),
    #Item(80, 4),
    #Item(80, 5),
    #Item(100, 8)]

#print(max_value(items, 10))

# dp is a dictionary used for memorization

