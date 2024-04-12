class Vector:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self): 
        return "Vector({}, {}, {})".format(self.x, self.y, self.z)       # return string "Vector(x, y, z)"

    def __eq__(self, other): 
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __ne__(self, other):        # v != w
        return not self == other

    def __add__(self, other):   # v + w
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other): 
        return self.x*other.x + self.y*other.y + self.z*other.z  

    def cross(self, other):   # return the cross product (Vector)
        return Vector(self.y*other.z - self.z*other.y,
                      self.z*other.x - self.x*other.z,
                      self.x*other.y - self.y*other.x)

    def length(self):    # the length of the vector
        return (self*self)**0.5

    def __hash__(self):   # we assume that vectors are immutable
        return hash((self.x, self.y, self.z))   # recommended
    
import math
v = Vector(2, 3, 5)
w = Vector(0, -7, 2)
assert v != w
assert v + w == Vector(2, -4, 7)
assert v - w == Vector(2, 10, 3)
assert v * w == -11
assert v.cross(w) == Vector(41, -4, -14)
assert v.length() == math.sqrt(38)
S = set([v, v, w])
assert len(S) == 2

print("Tests passed")
