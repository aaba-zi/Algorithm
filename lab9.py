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
        return Vec(self.x * scale, self.y * scale)
        
    def dot(self, other):
	"""dot times"""
        return self.x * other.x + self.y * other.y
        
    def lensq(self):
	"""length"""
        return self.dot(self)

    def __repr__(self):
	"""string"""
        return "({}, {})".format(self.x, self.y)
    
class PointSortKey:
    def __init__(self, p, anchor):
        self.vec = p - anchor       # Direction vector from anchor to p
        self.is_anchor = self.vec.lensq() == 0 # True iff p == anchor
   
    def __lt__(self, other):
        """Compares two sort keys. p1 < p2 means the vector from the
           anchor point to p2 is to the left of the vector from the
           anchor to p1.
        """
        if self.is_anchor:
            return True   # Ensure anchor point < all other points
        elif other.is_anchor:
            return False  # Ensure no other point < the anchor
        else:
            area = self.vec.x * other.vec.y - other.vec.x * self.vec.y
            return area > 0  #area > 0 => is_ccw => p1 < p2


def signed_area(a, b, c):
    """Twice the area of the triangle abc.
       Positive if abc are in counter clockwise order.
       Zero if a, b, c are collinear.
       Otherwise negative.
    """
    p = b - a
    q = c - a
    return p.x * q.y - q.x * p.y

def is_on_segment(p, a, b):
    """on line"""
    if signed_area(p, a, b) == 0:
        lenab = (a-b).lensq()
        lenpa = (p-a).lensq()
        lenpb = (p-b).lensq()
        if  lenpa <= lenab and lenpb <= lenab:
            return True
    return False

def is_ccw(a, b, c):
    """True iff triangle abc is counter-clockwise"""
    area = signed_area(a, b, c) # As earlier
	 # May want to throw an exception if area == 0
    return area > 0


def intersecting(a, b, c, d):
    """s"""
    if is_ccw(a, d, b) != is_ccw(a, c, b):
        if is_ccw(c, a, d) != is_ccw(c, b, d):
            return True
    return False

def is_strictly_convex(points):
    """s"""
    for i in range(len(points)-2):
        if is_ccw(points[i], points[i+1], points[i+2]) == False:
            return False
    return True

def gift_wrap(points):
    '''returns the convex hull of the points, computed using the Gift Wrap (Jarvis  March)'''
    bottommost = points[0] 
    for i, vec in enumerate(points):
        if vec.y < bottommost.y:
            bottommost = vec
        elif vec.y == bottommost.y:
            if vec.x < bottommost.x:
                bottommost = vec
    hull = [bottommost] #首先找出最左边的点 如果最左边的点有多个 则选择y最小的
    while len(hull) < 2 or hull[-1] != hull[0]: #只有>2且首尾相连就成立
        candidate = None
        for p in points:
            if p == hull[-1]:
                continue
            if candidate is None: #选择候选 
                candidate = p
            else:
                if is_ccw(hull[-1], candidate, p) == False: #判断是不是其余所有的点都在这个候选的左边
                    candidate = p
        hull.append(candidate)
    hull.pop() #跳出首尾相同的一个点
    return hull

def simple_polygon(points):
    '''eturns a simple polygon that passes through all points'''
    anchor = min(points, key=lambda p: (p.y, p.x))#找y最小的点
    simply_poly = sorted(points, key=lambda p: PointSortKey(p, anchor)) #排序
    #print(simply_poly)
    return simply_poly

def graham_scan(points):
    """returns the convex hull of the points as a list of points of type Vec."""
    simply_poly = simple_polygon(points)
    stack = [simply_poly[0], simply_poly[1], simply_poly[2]]#初始栈有3个元素
    for i in range(3, len(simply_poly)):
        while not is_ccw(stack[-2], stack[-1], simply_poly[i]):#如果点在线的右边 则出栈
            stack.pop()   
        stack.append(simply_poly[i])#直到在线的左边
    return stack    
    
