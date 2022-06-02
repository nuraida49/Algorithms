class Vec:
    """A simple vector in 2D. Also used as a position vector for points"""
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __add__(self, other):
        return Vec(self.x + other.x, self.y + other.y)
        
    def __sub__(self, other):
        return Vec(self.x - other.x, self.y - other.y)
        
    def dot(self, other):
        return self.x * other.x + self.y * other.y
        
    def lensq(self):
        return self.dot(self)

    def __str__(self):
        return "({}, {})".format(self.x, self.y)
    
fredsville = Vec(10, 20)
maryton = Vec(100, 200)
pounamu = Vec(70, 50)
p = pounamu + (maryton - (fredsville))
print(p)

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
    vector1 = a-p
    vector2 = b-p
    area = vector1.x * vector2.y - vector1.y * vector2.x
    if area == 0:
        lengthsquared = (b-a).lensq()
        if (a-p).lensq() <= lengthsquared and (b-p).lensq() <= lengthsquared:
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
    if len(vertices) < 3:
            return False
    for i in range(len(vertices)):
        a = vertices[i]
        b = vertices[(i + 1) % len(vertices)]
        c = vertices[(i + 2) % len(vertices)]
        if (not is_ccw(a, b, c)):
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
            if (candidate is None) or (is_ccw(hull[-1], p, candidate)):  # ** FIXME **
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
    
#points = [
    #Vec(1, 1),
    #Vec(99, 1),
    #Vec(100, 100),
    #Vec(99, 99),
    #Vec(0, 100),
    #Vec(100, 0),
    #Vec(1, 99),
    #Vec(0, 0),
    #Vec(50, 50)]
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
    """returns a simple polygon that passes through all points"""
    points = list(points)
    points.sort(key=lambda p: [p.y, p.x])
    anchor = points[0]
    simple = sorted(points, key=lambda p: PointSortKey(p, anchor))
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
    
#points = [
    #Vec(100, 100),
    #Vec(0, 100),
    #Vec(100, 0),
    #Vec(0, 0),
    #Vec(49, 50)]
#verts = graham_scan(points)
#for v in verts:
    #print(v)