import copy
def change_greedy(amount,coinage):
    amount_copy=copy.copy(amount)
    result=[]
    for coin in sorted( coinage,reverse=True):
        if amount//coin !=0:
            result.append((amount//coin,coin))
        amount=amount%coin
    total=0
    for i in result:
        total=total+ i[0]*i[1]
    if total==amount_copy:
        return result
    else:
        return None   
#print(change_greedy(82, [1, 10, 25, 5]))
#print(change_greedy(80, [1, 10, 25]))
#print(change_greedy(82, [10, 25, 5]))

def function(a):
    return a[1]+a[2]

def print_shows(show_list):
    show_list.sort(key=function)
    t_current=0
    for i in show_list:
        if i[1]>=t_current:
            print(i[0],i[1],i[1]+i[2])
            t_current=i[1]+i[2]
            
## The example from the lecture notes
#print_shows([
    #('a', 0, 6),
    #('b', 1, 3),
    #('c', 3, 2),
    #('d', 3, 5),
    #('e', 4, 3),
    #('f', 5, 4),
    #('g', 6, 4), 
    #('h', 8, 3)])
            
def fractional_knapsack(capacity, items):
    total = 0
    result = 0
    values = {}
    item = {}
    answer = []
    for stuff in items:
        (name, value, weight) = stuff
        benefit_weight = value / weight
        answer.append(benefit_weight)
        values[benefit_weight] = name
        item[name] = weight
        
    for stuffs in sorted(answer, reverse=True):
        name = values[stuffs]
        weight = item[name]
        if total < capacity and weight+total <= capacity:
            add_value = stuffs * weight
            total += weight
            result += add_value
        else:
            new = capacity - total
            add = new * stuffs
            result += add
            total += new
              
    return result

    
# The example from the lecture notes
#items = [
    #("Chocolate cookies", 20, 5),
    #("Potato chips", 15, 3),
    #("Pizza", 14, 2),
    #("Popcorn", 12, 4)]
#print(fractional_knapsack(9, items))

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
    cache = dict()

    def cell_cost(row, col):
        """The cost of getting to a given cell in the current grid."""
        if row < 0 or row >= n_rows or col < 0 or col >= n_cols:
            return INFINITY  # Off-grid cells are treated as infinities
        else:
            cost = grid[row][col]
            if row != 0:
                cost += min(cell_cost(row - 1, col + delta_col) for delta_col in range(-1, 2))
            return cost
            
    best = min(cell_cost(n_rows - 1, col) for col in range(n_cols))
    return best
    
    
def file_cost(filename):
    """The cheapest cost from row 1 to row n (1-origin) in the grid of integer
       weights read from the given file
    """
    return grid_cost(read_grid(filename))

print(file_cost('checkerboard.trivial.in'))
print(file_cost('checkerboard.small.in'))



