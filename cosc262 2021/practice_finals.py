# Do not alter the next two lines
from collections import namedtuple
Node = namedtuple("Node", ["value", "left", "right"])

# Rewrite the following function to avoid slicing
def binary_search_tree(nums, is_sorted=False, left=None, right=None):
    """Return a balanced binary search tree with the given nums
       at the leaves. is_sorted is True if nums is already sorted.
       Inefficient because of slicing but more readable.
    """
    if left is None:
        left = 0
        right = len(nums)
    if not is_sorted:
        nums = sorted(nums)
    n = right-left
    mid = (right+left)//2
    if n == 1:
        tree = Node(nums[mid], None, None)  # A leaf
    else:
        left = binary_search_tree(nums, True, left, mid)
        right = binary_search_tree(nums, True, mid, right)
        tree = Node(nums[mid - 1], left, right)
    return tree
    
# Leave the following function unchanged
def print_tree(tree, level=0):
    """Print the tree with indentation"""
    if tree.left is None and tree.right is None: # Leaf?
        print(2 * level * ' ' + f"Leaf({tree.value})")
    else:
        print(2 * level * ' ' + f"Node({tree.value})")
        print_tree(tree.left, level + 1)
        print_tree(tree.right, level + 1)
        
        
#nums = [22, 41, 19, 27, 12, 35, 14, 20,  39, 10, 25, 44, 32, 21, 18]
#tree = binary_search_tree(nums)
#print_tree(tree)

#nums = [228]
#tree = binary_search_tree(nums)
#print_tree(tree)

#nums = [228, 227, 3]
#tree = binary_search_tree(nums)
#print_tree(tree)

class Vec:
    """A simple vector in 2D. Can also be used as a position vector from
       origin to define points.
    """
    point_num = 0
    box_calls = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.label = 'P' + str(Vec.point_num)
        Vec.point_num += 1

    def __add__(self, other):
        """Vector addition"""
        return Vec(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """Vector subtraction"""
        return Vec(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scale):
        """Multiplication by a scalar"""
        return Vec(self.x * scale, self.y * scale)

    def dot(self, other):
        """Dot product"""
        return self.x * other.x + self.y * other.y

    def lensq(self):
        """The square of the length"""
        return self.dot(self)

    def in_box(self, bottom_left, top_right):
        """True iff this point (warning, not a vector!) lies within or on the
           boundary of the given rectangular box area"""
        Vec.box_calls += 1
        return bottom_left.x <= self.x <= top_right.x and bottom_left.y <= self.y <= top_right.y

    def __getitem__(self, axis):
        return self.x if axis == 0 else self.y

    def __repr__(self):
        return "({}, {})".format(self.x, self.y)
        
    def __lt__(self, other):
        """Less than operator, for sorting"""
        return (self.x, self.y) < (other.x, other.y)
        
    
class KdTree:
    """A 2D k-d tree"""
    LABEL_POINTS = True
    LABEL_OFFSET_X = 0.25
    LABEL_OFFSET_Y = 0.25    
    def __init__(self, points, depth=0, max_depth=10):
        """Initialiser, given a list of points, each of type Vec, the current
           depth within the tree (0 for the root) and the maximum depth
           allowable for a leaf node.
        """
        if len(points) < 2 or depth >= max_depth: # Ensure at least one point per leaf
            self.is_leaf = True
            self.points = points
        else:
            self.is_leaf = False
            self.axis = depth % 2  # 0 for vertical divider (x-value), 1 for horizontal (y-value)
            points = sorted(points, key=lambda p: p[self.axis])
            halfway = len(points) // 2
            self.coord = points[halfway - 1][self.axis]
            self.leftorbottom = KdTree(points[:halfway], depth + 1, max_depth)
            self.rightortop = KdTree(points[halfway:], depth + 1, max_depth)
            
    def points_in_range(self, query_rectangle):
        """Return a list of all points in the tree 'self' that lie within or
           on the boundary of the given query rectangle, which is defined by
           a pair of points (bottom_left, top_right), both of which are Vecs.
        """
        matches = []
        if self.is_leaf:
            for point in self.points:
                if point.in_box(query_rectangle[0], query_rectangle[1]):
                    matches.append(point)
        else:
            if self.axis == 0:
                if query_rectangle[1].x >= self.coord:
                    matches += self.rightortop.points_in_range(query_rectangle)
                if query_rectangle[0].x <= self.coord:
                    matches += self.leftorbottom.points_in_range(query_rectangle)
            else:
                if query_rectangle[1].y >= self.coord:
                    matches += self.rightortop.points_in_range(query_rectangle)
                if query_rectangle[0].y <= self.coord:
                    matches += self.leftorbottom.points_in_range(query_rectangle)
        return matches
    
    
    def plot(self, axes, top, right, bottom, left, depth=0):
        """Plot the the kd tree. axes is the matplotlib axes object on
           which to plot, top, right, bottom, left are the coordinates of
           the bounding box of the plot.
        """

        if self.is_leaf:
            axes.plot([p.x for p in self.points], [p.y for p in self.points], 'bo')
            if self.LABEL_POINTS:
                for p in self.points:
                    axes.annotate(p.label, (p.x, p.y),
                    xytext=(p.x + self.LABEL_OFFSET_X, p.y + self.LABEL_OFFSET_Y))
        else:
            if self.axis == 0:
                axes.plot([self.coord, self.coord], [bottom, top], '-', color='gray')
                self.leftorbottom.plot(axes, top, self.coord, bottom, left, depth + 1)
                self.rightortop.plot(axes, top, right, bottom, self.coord, depth + 1)
            else:
                axes.plot([left, right], [self.coord, self.coord], '-', color='gray')
                self.leftorbottom.plot(axes, self.coord, right, bottom, left, depth + 1)
                self.rightortop.plot(axes, top, right, self.coord, left, depth+1)
        if depth == 0:
            axes.set_xlim(left, right)
            axes.set_ylim(bottom, top)
       
    
    def __repr__(self, depth=0):
        """String representation of self"""
        if self.is_leaf:
            return depth * 2 * ' ' + "Leaf({})".format(self.points)
        else:
            s = depth * 2 * ' ' + "Node({}, {}, \n".format(self.axis, self.coord)
            s += self.leftorbottom.__repr__(depth + 1) + '\n'
            s += self.rightortop.__repr__(depth + 1) + '\n'
            s += depth * 2 * ' ' + ')'  # Close the node's opening parens
            return s
        
#point_tuples = [(1, 3), (10, 20), (5, 19), (0, 11), (15, 22), (30, 5)]
#points = [Vec(*tup) for tup in point_tuples]
#tree = KdTree(points)
#in_range = tree.points_in_range((Vec(0, 3), Vec(5, 19)))
#print(sorted(in_range))

class Vec:
    """A simple vector in 2D. Also used as a position vector for points"""
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __add__(self, other):
        return Vec(self.x + other.x, self.y + other.y)
        
    def __sub__(self, other):
        return Vec(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scale):
        """Multiplication by a scalar"""
        return Vec(self.x * scale, self.y * scale)
        
    def dot(self, other):
        return self.x * other.x + self.y * other.y
        
    def lensq(self):
        return self.dot(self)

    def __str__(self):
        return "({}, {})".format(self.x, self.y)
    
#fredsville = Vec(10, 20)
#maryton = Vec(100, 200)
#pounamu = Vec(70, 50)
#p = pounamu + (maryton-fredsville)
#print(p)

class Vec:
    """A simple vector in 2D. Also used as a position vector for points"""
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __add__(self, other):
        return Vec(self.x + other.x, self.y + other.y)
        
    def __sub__(self, other):
        return Vec(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scale):
        """Multiplication by a scalar"""
        return Vec(self.x * scale, self.y * scale)
        
    def dot(self, other):
        return self.x * other.x + self.y * other.y
        
    def lensq(self):
        return self.dot(self)

    def __str__(self):
        return "({}, {})".format(self.x, self.y)
        
        
def signed_area(a, b, c):
    """Twice the area of the triangle abc.
       Positive if abc are in counter clockwise order.
       Zero if a, b, c are colinear.
       Otherwise negative.
    """
    p = b - a
    q = c - a
    return p.x * q.y - q.x * p.y

def is_on_segment(p, a, b):
    pa = (p-a).lensq()
    ab = (a-b).lensq()
    pb = (p-b).lensq()
    if signed_area(p, a, b) == 0:
        if (pa <= ab) and (pb <= ab):
            return True
    return False
        
#a = Vec(1000, 2000)
#b = Vec(0, 0)
#p = Vec(500, 1000)
#print(is_on_segment(p, a, b))

#a = Vec(0, 0)
#b = Vec(1000, 2000)
#point_tuples = [
    #(-1, -1),
    #(-1, -2),
    #(-1000, -2000),
    #(0, 0),
    #(1, 2),
    #(500, 1000),
    #(500, 1001),
    #(500, 999),
    #(1000, 2000),
    #(1001, 2001),
    #(1001, 2002),
    #(2000, 4000)]
#points = [Vec(p[0], p[1]) for p in point_tuples]
#for p in points:
    #print(p, is_on_segment(p, a, b))
    
class Vec:
    """A simple vector in 2D. Can also be used as a position vector from
       origin to define points.
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        """Return this point/vector as a string in the form "(x, y)" """
        return "({}, {})".format(self.x, self.y)

    def __add__(self, other):
        """Vector addition"""
        return Vec(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """Vector subtraction"""
        return Vec(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scale):
        """Multiplication by a scalar"""
        return Vec(self.x * scale, self.y * scale)

    def dot(self, other):
        """Dot product"""
        return self.x * other.x + self.y * other.y

    def lensq(self):
        """The square of the length"""
        return self.dot(self)


def is_ccw(a, b, c):
    """True iff triangle abc is counter-clockwise."""
    p = b - a
    q = c - a
    area = p.x * q.y - q.x * p.y
    # May want to throw an exception if area == 0
    return area > 0

def classify_points(line_start, line_end, points):
    """P"""
    countleft=0
    countright=0
    for point in points:
        if is_ccw(line_start, line_end, point) is False:
            countright += 1
        else:
            countleft += 1
    return (countright, countleft)

#points = [
    #Vec(1, 99),
    #Vec(0, 100),
    #Vec(50, 0),
    #Vec(50, 1),
    #Vec(50, 99),
    #Vec(50, 50),
    #Vec(100, 100),
   #Vec(99, 99)]

#print(classify_points(Vec(0, 49), Vec(100, 49), points))

class Vec:
    """A simple vector in 2D. Also use for points (position vector)"""
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __add__(self, other):
        return Vec(self.x + other.x, self.y + other.y)
        
    def __sub__(self, other):
        return Vec(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scale):
        """Multiplication by a scalar"""
        return Vec(self.x * scale, self.y * scale)
        
    def dot(self, other):
        return self.x * other.x + self.y * other.y
        
    def lensq(self):
        return self.dot(self)
        
        
def is_ccw(a, b, c):
    """True iff triangle abc is counter-clockwise"""
    p = b - a
    q = c - a
    area = p.x * q.y - q.x * p.y
    # May want to throw an exception if area == 0
    return area > 0 

def intersecting(a, b, c, d):
    return (is_ccw(a,d,b) != is_ccw(a,c,b)) and (is_ccw(c,a,d) != is_ccw(c,b,d))

#a = Vec(0, 0)
#b = Vec(100, 0)
#c = Vec(101, 1)
#d = Vec(101, -1)
#print(intersecting(a, b, c, d))

#a = Vec(0, 0)
#b = Vec(100, 0)
#c = Vec(99, 1)
#d = Vec(99, -1)
#print(intersecting(a, b, c, d))

class Vec:
    """A simple vector in 2D. Also use for points (position vector)"""
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __add__(self, other):
        return Vec(self.x + other.x, self.y + other.y)
        
    def __sub__(self, other):
        return Vec(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scale):
        """Multiplication by a scalar"""
        return Vec(self.x * scale, self.y * scale)
        
    def dot(self, other):
        return self.x * other.x + self.y * other.y
        
    def lensq(self):
        return self.dot(self)
        
        
def is_ccw(a, b, c):
    """True iff triangle abc is counter-clockwise"""
    p = b - a
    q = c - a
    area = p.x * q.y - q.x * p.y
    # May want to throw an exception if area == 0
    return area > 0 

def is_strictly_convex(vertices):
    """P"""
    for i in range(len(vertices)):
        a = vertices[i]
        b = vertices[(i+1) % len(vertices)]
        c = vertices[(i+2) % len(vertices)]
        if is_ccw(a,b,c) is False:
            return False        
    return True

#verts = [
    #(0, 0),
    #(100, 0),
    #(100, 100),
    #(0, 100)]
#points = [Vec(v[0], v[1]) for v in verts]
#print(is_strictly_convex(points))

#verts = [
    #(0, 0),
    #(0, 100),
    #(100, 100),
    #(100, 0)]
#points = [Vec(v[0], v[1]) for v in verts]
#print(is_strictly_convex(points))

#verts = [
    #(60, 60),
    #(100, 0),
    #(100, 100),
    #(0, 100)]
#points = [Vec(v[0], v[1]) for v in verts]
#print(is_strictly_convex(points))

class Vec:
    """A simple vector in 2D. Can also be used as a position vector from
       origin to define points.
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        """Return this point/vector as a string in the form "(x, y)" """
        return "({}, {})".format(self.x, self.y)

    def __add__(self, other):
        """Vector addition"""
        return Vec(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """Vector subtraction"""
        return Vec(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scale):
        """Multiplication by a scalar"""
        return Vec(self.x * scale, self.y * scale)

    def dot(self, other):
        """Dot product"""
        return self.x * other.x + self.y * other.y

    def lensq(self):
        """The square of the length"""
        return self.dot(self)


def is_ccw(a, b, c):
    """True iff triangle abc is counter-clockwise."""
    p = b - a
    q = c - a
    area = p.x * q.y - q.x * p.y
	 # May want to throw an exception if area == 0
    return area > 0 
    
        
def gift_wrap(points):
    """ Returns points on convex hull in CCW using the Gift Wrap algorithm"""
    # Get the bottom-most point (and left-most if necessary).
    assert len(points) >= 3
    bottommost = min(points, key=lambda p: (p.y, p.x))
    hull = [bottommost]
    done = False
    
    # Loop, adding one vertex at a time, until hull is (about to be) closed.
    while not done:
        candidate = None
        # Loop through all points, looking for the one that is "rightmost"
        # looking from last point on hull
        for p in points:
            if p is hull[-1]:
                continue
            if (candidate == None) or (is_ccw(hull[-1], p, candidate)):  # ** FIXME **
                candidate = p
        if candidate is bottommost:
            done = True    # We've closed the hull
        else:
            hull.append(candidate)

    return hull

#points = [
    #Vec(1, 99),
    #Vec(0, 100),
    #Vec(50, 0),
    #Vec(50, 1),
    #Vec(50, 99),
    #Vec(50, 50),
    #Vec(100, 100),
   #Vec(99, 99)]
#verts = gift_wrap(points)
#for v in verts:
    #print(v)
    
class Vec:
    """A simple vector in 2D. Can also be used as a position vector from
       origin to define points.
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y 

    def __repr__(self):
        """Return this point/vector as a string in the form "(x, y)" """
        return "({}, {})".format(self.x, self.y)

    def __add__(self, other):
        """Vector addition"""
        return Vec(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """Vector subtraction"""
        return Vec(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scale):
        """Multiplication by a scalar"""
        return Vec(self.x * scale, self.y * scale)

    def dot(self, other):
        """Dot product"""
        return self.x * other.x + self.y * other.y

    def lensq(self):
        """The square of the length"""
        return self.dot(self)

        
class PointSortKey:
    """A class for use as a key when sorting points wrt bottommost point"""
    def __init__(self, p, bottommost):
        """Construct an instance of the sort key"""
        self.direction = p - bottommost
        self.is_bottommost = self.direction.lensq() == 0  # True if p == bottommost
        
    def __lt__(self, other):
        """Compares two sort keys. p1 < p2 means the vector the from bottommost point
           to p2 is to the left of the vector from the bottommost to p1.
        """
        if self.is_bottommost:
            return True   # Ensure bottommost point is less than all other points
        elif other.is_bottommost:
            return False  # Ensure no other point is less than the bottommost
        else:
            area = self.direction.x * other.direction.y - other.direction.x * self.direction.y
            return area > 0
	
def simple_polygon(points):
    points.sort(key=lambda p:[p.y, p.x])
    anchor = points[0]
    simple = sorted(points, key=lambda p:PointSortKey(p, anchor))
    return simple

#points = [
    #Vec(100, 100),
    #Vec(0, 100),
    #Vec(50, 0)]
#verts = simple_polygon(points)
#for v in verts:
    #print(v)
    
#points = [
    #Vec(100, 100),
    #Vec(0, 100),
    #Vec(100, 0),
    #Vec(0, 0),
    #Vec(49, 50)]
#verts = simple_polygon(points)
#for v in verts:
    #print(v)
    

class Vec:
    """A simple vector in 2D. Can also be used as a position vector from
       origin to define points.
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        """Return this point/vector as a string in the form "(x, y)" """
        return "({}, {})".format(self.x, self.y)

    def __add__(self, other):
        """Vector addition"""
        return Vec(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """Vector subtraction"""
        return Vec(self.x - other.x, self.y - other.y)

    def dot(self, other):
        """Dot product"""
        return self.x * other.x + self.y * other.y

    def lensq(self):
        """The square of the length"""
        return self.dot(self)

    def __lt__(self, other):
        """For convenience we define '<' to mean
           "less than with respect to angle", i.e.
           the direction of self is less than the
           direction of other in a CCW sense."""
        area = self.x * other.y - other.x * self.y
        return area > 0
        
def simple_polygon(points):
    """Return the given list of points ordered so that connecting them in order
       yields a simple polygon"""
       
    # Firstly swap the bottommost (and if necessary leftmost) point to the
    # 0th position in the list. The first line finds the bottommost point,
    # and the next line finds its index, so it can be swapped to the front.
    bottommost = min(points, key=lambda p: (p.y, p.x))
    index = points.index(bottommost)
    points[0], points[index] = points[index], points[0]
    
    # Now just sort the rest by angle from points[0]
    rest = points[1:]
    rest.sort(key=lambda x: points[0] - x) 
    return [points[0]] + rest

def is_ccw(p0, p1, p2):
    """True if triangle p0, p1, p2 has vertices in counter-clockwise order"""
    return (p1 - p0) < (p2 - p0)    

def graham_scan(points):
    """does graham scan"""
    points = simple_polygon(points)
    stack = points[:3]
    for i in range(3, len(points)):
        while not is_ccw(stack[-2], stack[-1], points[i]):
            stack.pop()
        stack.append(points[i])
    return stack

#points = [
    #Vec(100, 100),
    #Vec(0, 100),
    #Vec(50, 0)]
#verts = graham_scan(points)
#for v in verts:
    #print(v)
    
def change_greedy(amount, coinage):
    coinage.sort(reverse=True)
    change = []
    for coin in coinage:
        coin_amount = 0
        while amount >= coin:
            amount -= coin
            coin_amount += 1
        if coin_amount > 0:
            change.append((coin_amount, coin))
    if amount != 0:
        return None
    else:
        return change
    
#print(change_greedy(82, [1, 10, 25, 5]))
#print(change_greedy(80, [1, 10, 25]))
#print(change_greedy(82, [10, 25, 5]))

def function(a):
    return a[1]+a[2]

def print_shows(show_list):
    show_list.sort(key=function)
    t_current=0
    for show in show_list:
        if show[1]>=t_current:
            print(show[0],show[1],show[1]+show[2])
            t_current=show[1]+show[2]
	    
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
    
	
def next_vertex(intree, distance):
    possible = []
    nextvert = None
    for index, vertex in enumerate(intree):
        if not vertex:
            possible.append(index)
    minweight = distance[possible[0]]
    nextvert = possible[0]
    for i in possible:
        weight = distance[i]
        if weight < minweight:
            minweight = weight
            nextvert = i
    return nextvert

def dijkstra(adj_list, start):
    n = len(adj_list)
    in_tree = [False] * n
    distance = [float('inf')] * n
    parent = [None] * n
    distance[start] = 0
    while not all(in_tree):
        u = next_vertex(in_tree, distance)
        in_tree[u] = True
        for v, weight in adj_list[u]:
            if not in_tree[v] and distance[u] + weight < distance[v]:
                distance[v] = distance[u] + weight
                parent[v] = u
    return parent, distance
    
def fractional_knapsack(capacity, items):
    weight = []
    benefit = []
    value = []
    result = 0
    items.sort(reverse = True, key=lambda x: x[1]/x[2]) #sort items in decensing order of benefit
    for item in items:
        value.append(item[1])
        weight.append(item[2])
        benefit.append(item[1]/item[2])
    fractions = [0]*len(value)
    for i in range(len(value)):
        if weight[i] <= capacity:
            fractions[i] = 1
            result += value[i]
            capacity -= weight[i]
        else:
            fractions[i] = capacity/weight[i]
            result += value[i]*capacity/weight[i]
            break
    return result
## The example from the lecture notes
#items = [
    #("Chocolate cookies", 20, 5),
    #("Potato chips", 15, 3),
    #("Pizza", 14, 2),
    #("Popcorn", 12, 4)]
#print(fractional_knapsack(9, items))
	    
def distance_matrix(adj_list):
    n = len(adj_list)
    resultant_matrix = [([float('inf')] * n) for i in range(n)]
    for i in range(n):
        resultant_matrix[i][i] = 0
    for i in range(n):
        for k, v in adj_list[i]:
            resultant_matrix[i][k] = v
    return resultant_matrix

def radix_sort(numbers, d):
    n = 10
    for i in range(d):
	numbers = counting_sort(numbers, lambda x: x%n)
	n *= 10
    return numbers

def all_paths(adj_list, source, destination):
    adjacency = adjacency_list(adj_list)
    state = ["U" for i in range(len(adjacency))]
    result = []
    dfs_backtrack(adjacency, state, source, destination, result)
    return result

def radix_sort(numbers, d):
    n = 10
    for i in range(d):
	numbers = counting_sort(numbers, lambda x: x%n)
	n *= 10
    return numbers

def change_greedy(amount,coinage):
    coinage.sort(reverse=True)
    change = []
    for coin in coinage:
	coinamount = 0
	while amount >= coin:
	    amount -= coin
	    coinamount += 1
	if cointamount > 0:
	    change.append((coinamount, coin))
    if amount != 0:
	return None
    else:
	return change
    
def change_greedy(amount, coinage):
    coinage.sort(reverse=True)
    change = []
    for coin in coinage:
	coinamount = 0
	while amount >= coin:
	    amount -= coin
	    coinamount += 1
	if coinamount > 0:
	    change.append((coinamount, coin))
    if amount != 0:
	return None
    else:
	return change
    
def coins_reqd(value, coinage):
    alist = []
    aDict = dict()
    if not coinage or value <= 0:
	return alist
    else:
	alist = min((coins_reqd(value-c, coinage) + [c] for c in coinage if value >= c), key=len)
    return alist

def all_paths(graph_string, source, destination):
    adj_list = adjacency_list(graph_string)
    path = []
    result = find_all_paths(adj_list, source, destination, path)
    return result

def find_all_paths(adj_list, source, destination, path):
    path = path + [source]
    if source == destination:
        return [path]
    result = []
    for vertex in adj_list[source]:
        if vertex not in path:
            newresult = find_all_paths(adj_list, vertex, destination, path)
            for newpath in newresult:
                result.append(newpath)
    return result

def simple_polygon(points):
    bottommost = min(points, key=lambda p: (p.y, p.x))
    index = points.index(bottommost)
    points[0], points[index] = points[index], points[0]
    rest = points[1:]
    rest.sort(key=lambda x: points[0]-x)
    return [points[0]] + rest

def simple_polygon(points):
    bottommost = min(points, key=lambda p: (p.y, p.x))
    index = points.index(bottommost)
    points[0], points[index] = points[index], points[0]
    rest = points[1:]
    rest.sort(key=lambda x: points[0] - x)
    return [points[0]] + rest

def binary_search_tree(nums, is_sorted=False, left=None, right=None):
    """Return a balanced binary search tree with the given nums
       at the leaves. is_sorted is True if nums is already sorted.
       Inefficient because of slicing but more readable.
    """
    if left is None:
        left = 0
        right = len(nums)
    if not is_sorted:
        nums = sorted(nums)
    n = right-left
    mid = (right+left)//2
    if n == 1:
        tree = Node(nums[mid], None, None)  # A leaf
    else:
        left = binary_search_tree(nums, True, left, mid)
        right = binary_search_tree(nums, True, mid, right)
        tree = Node(nums[mid - 1], left, right)
    return tree

def path_length(parent, start, end):
    length = 0
    cur = end
    while cur != start:
	if cur is None:
	    return float('inf')
	length += 1
	cur = parent[cur]
    return length

#print(path_length([None, 0], 0, 1))

def fractional_knapsack(capacity, items):
    items.sort(items, key=lambda x: x[1]/x[2], reverse=True)
    total = 0
    for _, value, weight in items:
	if weight <= capacity:
	    total += value
	    capacity -= weight
	else:
	    total += capacity/weight*value
	    break
    return total

def longest_common_subsequence(list1, list2):
    if not list1 or not list2:
	return []
    if list1[0] == list2[0]:
	return [list1[0]] + longest_common_subsequence(list1[1:], list2[1:])
    option1 = longest_common_subsequence(list1[1:], list2)
    option2 = longest_common_subsequence(list1, list2[1:])
    return option1 if len(option1) >= len(option2) else option2

num_calls = 0  # Global counter of mat_mul calls

def mat_mul(m1, m2):
    """Return m1 * m2 where m1 and m2 are square matrices of numbers, represented
       as lists of lists.
    """
    global num_calls # Counter of calls (for marking)
    num_calls += 1   # Increment the count of calls
    n = len(m1)    # Size of the matrix
    assert len(m1[0]) == n and len(m2) == n and len(m2[0]) == n
    mprod = [[sum(m1[i][k] * m2[k][j] for k in range(n)) for j in range(n)]
        for i in range(n)]
    return mprod

def mat_power(m, p):
    if p == 1:
	return m
    half = mat_power(m, p//2)
    if p % 2 == 1:
	return mat_mul(half, mat_mul(half, m))
    else:
	return mat_mul(half, half)
    
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
	return INFINITY  # Off grid cells are treated as infinities
    elif (row,col) in cache.keys(): #if row,col value is already in cache, use it 
	return cache[(row,col)]     #instead of calculating it again
    else:
	cost = grid[row][col]
	if row != 0:
	    cost += min(cell_cost(row - 1, col + delta_col) for delta_col in range(-1, 2))
	    cache[(row, col)] = cost #add calculated cost to cache for reuse
	return cost
    best = min(cell_cost(n_rows - 1, col) for col in range(n_cols))
    return best
    
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
            return INFINITY  # Off grid cells are treated as infinities
        elif (row,col) in cache.keys(): #if row,col value is already in cache, use it 
            return cache[(row,col)]     #instead of calculating it again
        else:
            cost = grid[row][col]
            if row != 0:
                cost += min(cell_cost(row - 1, col + delta_col) for delta_col in range(-1, 2))
                cache[(row, col)] = cost #add calculated cost to cache for reuse
            return cost
            
    best = min(cell_cost(n_rows - 1, col) for col in range(n_cols))
    return best